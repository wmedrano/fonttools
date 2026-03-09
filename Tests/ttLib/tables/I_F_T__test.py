import unittest
from fontTools.ttLib import newTable
from fontTools.misc.testTools import FakeFont

class IFTTableTest(unittest.TestCase):
    def test_decompile_compile_format1(self):
        for tag in ("IFT ", "IFTX"):
            with self.subTest(tag=tag):
                # IFT Format 1
                data = (
                    b"\x01" + # format=1
                    b"\x00\x00\x00" + # reserved=0
                    b"\x03" + # flags=3 (CFF and CFF2 offsets present)
                    b"\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04" + # compatibilityId
                    b"\x00\x0a" + # maxEntryIndex=10
                    b"\x00\x05" + # maxGlyphMapEntryIndex=5
                    b"\x00\x00\x0d" + # glyphNum=13
                    b"\x00\x00\x00\x36" + # glyphMapOffset=54
                    b"\x00\x00\x00\x00" + # featureMapOffset=0
                    b"\xaa\x55" + # appliedEntriesBitMap (2 bytes for maxEntryIndex=10)
                    b"\x00\x05" + # urlTemplateLength=5
                    b"https" + # urlTemplate
                    b"\x01" + # patchFormat=1
                    b"\x00\x00\x03\xe8" + # cffCharStringsOffset=1000
                    b"\x00\x00\x07\xd0" + # cff2CharStringsOffset=2000
                    # GlyphMap at offset 54
                    b"\x00\x0a" + # firstMappedGlyph=10
                    b"\x01\x02\x03" # entryIndex (3 elements for glyphNum=13 - 10)
                )

                table = newTable(tag)
                font = FakeFont(["glyph0", "glyph1", "glyph2", "glyph3", "glyph4", "glyph5", "glyph6", "glyph7", "glyph8", "glyph9", "glyph10", "glyph11", "glyph12"])
                table.decompile(data, font)

                self.assertEqual(table.table.Format, 1)
                self.assertEqual(table.table.CompatibilityId, [1, 2, 3, 4])
                self.assertEqual(table.table.GlyphNum, 13)
                self.assertEqual(table.table.GlyphMap.FirstMappedGlyph, 10)
                self.assertEqual(table.table.GlyphMap.EntryIndex, [1, 2, 3])
                self.assertEqual(table.table.URLTemplate, b"https")
                self.assertEqual(table.table.CFFCharStringsOffset, 1000)
                self.assertEqual(table.table.CFF2CharStringsOffset, 2000)
                self.assertEqual(table.table.AppliedEntriesBitMap, b"\xaa\x55")

                # Test compile
                compiled_data = table.compile(font)
                self.assertEqual(data, compiled_data)

    def test_decompile_compile_format1_maxEntryIndex_large(self):
        for tag in ("IFT ", "IFTX"):
            with self.subTest(tag=tag):
                # IFT Format 1 with maxEntryIndex >= 256
                data = (
                    b"\x01" + # format=1
                    b"\x00\x00\x00" + # reserved=0
                    b"\x00" + # flags=0
                    b"\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00\x04" + # compatibilityId
                    b"\x01\x00" + # maxEntryIndex=256
                    b"\x00\x05" + # maxGlyphMapEntryIndex=5
                    b"\x00\x00\x0c" + # glyphNum=12
                    b"\x00\x00\x00\x48" + # glyphMapOffset=72
                    b"\x00\x00\x00\x00" + # featureMapOffset=0
                    (b"\xff" * 33) +
                    b"\x00\x00" + # urlTemplateLength=0
                    b"\x01" # patchFormat=1
                )
                # Add GlyphMap
                data += (
                    b"\x00\x0a" + # firstMappedGlyph=10
                    b"\x00\x01\x00\x02" # entryIndex (2 elements, each 2 bytes because maxEntryIndex >= 256)
                )

                table = newTable(tag)
                font = FakeFont([f"glyph{i}" for i in range(12)])
                table.decompile(data, font)

                self.assertEqual(table.table.MaxEntryIndex, 256)
                self.assertEqual(table.table.GlyphMap.EntryIndex, [1, 2])
                self.assertEqual(len(table.table.AppliedEntriesBitMap), 33)

                compiled_data = table.compile(font)
                self.assertEqual(data, compiled_data)

    def test_decompile_compile_feature_map(self):
        for tag in ("IFT ", "IFTX"):
            with self.subTest(tag=tag):
                # IFT Format 1 with Feature Map
                data = (
                    b"\x01" + # format=1
                    b"\x00\x00\x00" + # reserved=0
                    b"\x00" + # flags=0
                    (b"\x00" * 16) + # compatibilityId
                    b"\x00\x0a" + # maxEntryIndex=10
                    b"\x00\x00" + # maxGlyphMapEntryIndex=0
                    b"\x00\x00\x00" + # glyphNum=0
                    b"\x00\x00\x00\x00" + # glyphMapOffset=0
                    b"\x00\x00\x00\x29" + # featureMapOffset=41
                    b"\x00\x00" + # appliedEntriesBitMap (2 bytes for maxEntryIndex=10)
                    b"\x00\x00" + # urlTemplateLength=0
                    b"\x01" + # patchFormat=1
                    # FeatureMap at offset 41
                    b"\x00\x02" + # featureCount=2
                    # FeatureRecord 0
                    b"test" + # featureTag='test'
                    b"\x01" + # firstNewEntryIndex=1
                    b"\x01" + # entryMapNum=1
                    # FeatureRecord 1
                    b"demo" + # featureTag='demo'
                    b"\x02" + # firstNewEntryIndex=2
                    b"\x02" + # entryMapNum=2
                    # EntryMapRecords (1 + 2 = 3 records)
                    b"\x01\x02" + # rec 0: first=1, last=2
                    b"\x03\x04" + # rec 1: first=3, last=4
                    b"\x05\x06" # rec 2: first=5, last=6
                )

                table = newTable(tag)
                font = FakeFont([])
                table.decompile(data, font)

                self.assertEqual(table.table.FeatureMap.FeatureCount, 2)
                self.assertEqual(table.table.FeatureMap.FeatureRecords[0].FeatureTag, "test")
                self.assertEqual(table.table.FeatureMap.FeatureRecords[1].FeatureTag, "demo")
                self.assertEqual(len(table.table.FeatureMap.EntryMapRecords), 3)
                self.assertEqual(table.table.FeatureMap.EntryMapRecords[0].FirstEntryIndex, 1)
                self.assertEqual(table.table.FeatureMap.EntryMapRecords[2].LastEntryIndex, 6)

                compiled_data = table.compile(font)
                self.assertEqual(data, compiled_data)

    def test_decompile_compile_format2(self):
        for tag in ("IFT ", "IFTX"):
            with self.subTest(tag=tag):
                # IFT Format 2
                data = (
                    b"\x02" + # format=2
                    b"\x00\x00\x00" + # reserved=0
                    b"\x03" + # flags=3 (CFF and CFF2 offsets present)
                    (b"\x01\x02\x03\x04" * 4) + # compatibilityId (16 bytes)
                    b"\x01" + # defaultPatchFormat=1
                    b"\x00\x00\x05" + # entryCount=5
                    b"\x00\x00\x00\x00" + # entriesOffset=0
                    b"\x00\x00\x00\x00" + # entryIdStringDataOffset=0
                    b"\x00\x05" + # urlTemplateLength=5
                    b"https" + # urlTemplate
                    b"\x00\x00\x03\xe8" + # cffCharStringsOffset=1000
                    b"\x00\x00\x07\xd0"   # cff2CharStringsOffset=2000
                )

                table = newTable(tag)
                font = FakeFont([])
                table.decompile(data, font)

                ot_table = table.table
                self.assertEqual(ot_table.Format, 2)
                self.assertEqual(ot_table.DefaultPatchFormat, 1)
                self.assertEqual(ot_table.EntryNum, 5)
                self.assertEqual(ot_table.URLTemplate, b"https")
                self.assertEqual(ot_table.CFFCharStringsOffset, 1000)
                self.assertEqual(ot_table.CFF2CharStringsOffset, 2000)

                # Test compile
                compiled_data = table.compile(font)
                self.assertEqual(data, compiled_data)

    def test_unsupported_format(self):
        for tag in ("IFT ", "IFTX"):
            with self.subTest(tag=tag):
                data = b"\x03\x00\x00\x00\x00" # Format 3
                table = newTable(tag)
                font = FakeFont([])
                table.decompile(data, font)
                self.assertEqual(table.table.Format, 3)
                # Ensure it doesn't have attributes from Format 1 or 2
                self.assertFalse(hasattr(table.table, "GlyphMap"))
                self.assertFalse(hasattr(table.table, "Entries"))

if __name__ == "__main__":
    unittest.main()
