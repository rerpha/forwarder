# automatically generated by the FlatBuffers compiler, do not modify

# namespace: 

import flatbuffers

class ArrayString(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAsArrayString(cls, buf, offset):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ArrayString()
        x.Init(buf, n + offset)
        return x

    # ArrayString
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ArrayString
    def Value(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.String(a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 4))
        return ""

    # ArrayString
    def ValueLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

def ArrayStringStart(builder): builder.StartObject(1)
def ArrayStringAddValue(builder, value): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(value), 0)
def ArrayStringStartValueVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def ArrayStringEnd(builder): return builder.EndObject()
