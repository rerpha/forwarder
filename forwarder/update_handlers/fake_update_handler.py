from random import randint

import numpy as np
from p4p.nt import NTScalar

from forwarder.kafka.kafka_producer import KafkaProducer
from forwarder.repeat_timer import RepeatTimer, milliseconds_to_seconds
from forwarder.update_handlers.base_update_handler import BaseUpdateHandler
from forwarder.update_handlers.schema_serialisers import schema_serialisers


class FakeUpdateHandler(BaseUpdateHandler):
    """
    Periodically generate a random integer as a PV value instead of monitoring a real EPICS PV
    serialises updates in FlatBuffers and passes them onto an Kafka Producer.
    """

    def __init__(
        self,
        producer: KafkaProducer,
        pv_name: str,
        output_topic: str,
        schema: str,
        fake_pv_period_ms: int,
    ):
        super().__init__(producer, pv_name, output_topic, schema, fake_pv_period_ms)
        self._schema = schema

        self._repeating_timer = RepeatTimer(
            milliseconds_to_seconds(fake_pv_period_ms), self._timer_callback
        )
        self._repeating_timer.start()

    def _timer_callback(self):
        if self._schema == "tdct":
            # tdct needs a 1D array as data to send
            data = np.array([randint(0, 100)]).astype(np.int32)
            update = NTScalar("ai").wrap(data)
        else:
            # Otherwise 0D (scalar) is fine
            update = NTScalar("i").wrap(randint(0, 100))
        try:
            for serialiser_tracker in self.serialiser_tracker_list:
                new_message, new_timestamp = serialiser_tracker.serialiser.pva_serialise(update)
                if new_message is not None:
                    serialiser_tracker.set_new_message(new_message, new_timestamp)
        except (RuntimeError, ValueError) as e:
            self._logger.error(
                f"Got error when handling PVA update. Message was: {str(e)}"
            )

    def stop(self):
        """
        Stop periodic updates
        """
        self._repeating_timer.cancel()
