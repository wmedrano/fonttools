from fontTools.ttLib import newTable
from fontTools.misc.testTools import parseXmlInto, getXML, FakeFont
import unittest

class IFTTTXTest(unittest.TestCase):
    def test_format1_roundtrip(self):
        ift_hex = ("010000000300000001000000020000000300000004000a000500000d0000003600000000aa550005687474707301000003e8000007d0000a010203")
        ift_binary = bytes.fromhex(ift_hex)
        table = newTable("IFT ")
        font = FakeFont([f"glyph{i}" for i in range(20)])
        table.decompile(ift_binary, font)
        xml_lines = getXML(table.toXML, font)
        xml_text = "\n".join(xml_lines)
        table2 = newTable("IFT ")
        if not hasattr(table2, "table"):
            from fontTools.ttLib.tables import otTables
            table2.table = getattr(otTables, "IFT ")()
        table2.table.Format = 1
        parseXmlInto(font, table2.table, xml_text)
        compiled_binary = table2.compile(font)
        self.assertEqual(ift_binary, compiled_binary)

if __name__ == "__main__":
    unittest.main()
