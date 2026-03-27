from .otSchema import OtDataField

otData = [
    #
    # common
    #
    ("LookupOrder", []),
    (
        "ScriptList",
        [
            OtDataField("uint16", "ScriptCount", description="Number of ScriptRecords"),
            OtDataField(
                "struct",
                "ScriptRecord",
                repeat="ScriptCount",
                aux=0,
                description="Array of ScriptRecords -listed alphabetically by ScriptTag",
            ),
        ],
    ),
    (
        "ScriptRecord",
        [
            OtDataField("Tag", "ScriptTag", description="4-byte ScriptTag identifier"),
            OtDataField(
                "Offset",
                "Script",
                description="Offset to Script table-from beginning of ScriptList",
            ),
        ],
    ),
    (
        "Script",
        [
            OtDataField(
                "Offset",
                "DefaultLangSys",
                description="Offset to DefaultLangSys table-from beginning of Script table-may be NULL",
            ),
            OtDataField(
                "uint16",
                "LangSysCount",
                description="Number of LangSysRecords for this script-excluding the DefaultLangSys",
            ),
            OtDataField(
                "struct",
                "LangSysRecord",
                repeat="LangSysCount",
                aux=0,
                description="Array of LangSysRecords-listed alphabetically by LangSysTag",
            ),
        ],
    ),
    (
        "LangSysRecord",
        [
            OtDataField(
                "Tag", "LangSysTag", description="4-byte LangSysTag identifier"
            ),
            OtDataField(
                "Offset",
                "LangSys",
                description="Offset to LangSys table-from beginning of Script table",
            ),
        ],
    ),
    (
        "LangSys",
        [
            OtDataField(
                "Offset",
                "LookupOrder",
                description="= NULL (reserved for an offset to a reordering table)",
            ),
            OtDataField(
                "uint16",
                "ReqFeatureIndex",
                description="Index of a feature required for this language system- if no required features = 0xFFFF",
            ),
            OtDataField(
                "uint16",
                "FeatureCount",
                description="Number of FeatureIndex values for this language system-excludes the required feature",
            ),
            OtDataField(
                "uint16",
                "FeatureIndex",
                repeat="FeatureCount",
                aux=0,
                description="Array of indices into the FeatureList-in arbitrary order",
            ),
        ],
    ),
    (
        "FeatureList",
        [
            OtDataField(
                "uint16",
                "FeatureCount",
                description="Number of FeatureRecords in this table",
            ),
            OtDataField(
                "struct",
                "FeatureRecord",
                repeat="FeatureCount",
                aux=0,
                description="Array of FeatureRecords-zero-based (first feature has FeatureIndex = 0)-listed alphabetically by FeatureTag",
            ),
        ],
    ),
    (
        "FeatureRecord",
        [
            OtDataField(
                "Tag", "FeatureTag", description="4-byte feature identification tag"
            ),
            OtDataField(
                "Offset",
                "Feature",
                description="Offset to Feature table-from beginning of FeatureList",
            ),
        ],
    ),
    (
        "Feature",
        [
            OtDataField(
                "Offset",
                "FeatureParams",
                description="= NULL (reserved for offset to FeatureParams)",
            ),
            OtDataField(
                "uint16",
                "LookupCount",
                description="Number of LookupList indices for this feature",
            ),
            OtDataField(
                "uint16",
                "LookupListIndex",
                repeat="LookupCount",
                aux=0,
                description="Array of LookupList indices for this feature -zero-based (first lookup is LookupListIndex = 0)",
            ),
        ],
    ),
    ("FeatureParams", []),
    (
        "FeatureParamsSize",
        [
            OtDataField(
                "DeciPoints",
                "DesignSize",
                description="The design size in 720/inch units (decipoints).",
            ),
            OtDataField(
                "uint16",
                "SubfamilyID",
                description="Serves as an identifier that associates fonts in a subfamily.",
            ),
            OtDataField("NameID", "SubfamilyNameID", description="Subfamily NameID."),
            OtDataField(
                "DeciPoints",
                "RangeStart",
                description="Small end of recommended usage range (exclusive) in 720/inch units.",
            ),
            OtDataField(
                "DeciPoints",
                "RangeEnd",
                description="Large end of recommended usage range (inclusive) in 720/inch units.",
            ),
        ],
    ),
    (
        "FeatureParamsStylisticSet",
        [
            OtDataField("uint16", "Version", description="Set to 0."),
            OtDataField("NameID", "UINameID", description="UI NameID."),
        ],
    ),
    (
        "FeatureParamsCharacterVariants",
        [
            OtDataField("uint16", "Format", description="Set to 0."),
            OtDataField(
                "NameID", "FeatUILabelNameID", description="Feature UI label NameID."
            ),
            OtDataField(
                "NameID",
                "FeatUITooltipTextNameID",
                description="Feature UI tooltip text NameID.",
            ),
            OtDataField(
                "NameID", "SampleTextNameID", description="Sample text NameID."
            ),
            OtDataField(
                "uint16",
                "NumNamedParameters",
                description="Number of named parameters.",
            ),
            OtDataField(
                "NameID",
                "FirstParamUILabelNameID",
                description="First NameID of UI feature parameters.",
            ),
            OtDataField(
                "uint16",
                "CharCount",
                description="Count of characters this feature provides glyph variants for.",
            ),
            OtDataField(
                "uint24",
                "Character",
                repeat="CharCount",
                aux=0,
                description="Unicode characters for which this feature provides glyph variants.",
            ),
        ],
    ),
    (
        "LookupList",
        [
            OtDataField(
                "uint16", "LookupCount", description="Number of lookups in this table"
            ),
            OtDataField(
                "Offset",
                "Lookup",
                repeat="LookupCount",
                aux=0,
                description="Array of offsets to Lookup tables-from beginning of LookupList -zero based (first lookup is Lookup index = 0)",
            ),
        ],
    ),
    (
        "Lookup",
        [
            OtDataField(
                "uint16",
                "LookupType",
                description="Different enumerations for GSUB and GPOS",
            ),
            OtDataField("LookupFlag", "LookupFlag", description="Lookup qualifiers"),
            OtDataField(
                "uint16",
                "SubTableCount",
                description="Number of SubTables for this lookup",
            ),
            OtDataField(
                "Offset",
                "SubTable",
                repeat="SubTableCount",
                aux=0,
                description="Array of offsets to SubTables-from beginning of Lookup table",
            ),
            OtDataField(
                "uint16",
                "MarkFilteringSet",
                aux="LookupFlag & 0x0010",
                description="If set, indicates that the lookup table structure is followed by a MarkFilteringSet field. The layout engine skips over all mark glyphs not in the mark filtering set indicated.",
            ),
        ],
    ),
    (
        "CoverageFormat1",
        [
            OtDataField(
                "uint16", "CoverageFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "uint16", "GlyphCount", description="Number of glyphs in the GlyphArray"
            ),
            OtDataField(
                "GlyphID",
                "GlyphArray",
                repeat="GlyphCount",
                aux=0,
                description="Array of GlyphIDs-in numerical order",
            ),
        ],
    ),
    (
        "CoverageFormat2",
        [
            OtDataField(
                "uint16", "CoverageFormat", description="Format identifier-format = 2"
            ),
            OtDataField("uint16", "RangeCount", description="Number of RangeRecords"),
            OtDataField(
                "struct",
                "RangeRecord",
                repeat="RangeCount",
                aux=0,
                description="Array of glyph ranges-ordered by Start GlyphID",
            ),
        ],
    ),
    (
        "RangeRecord",
        [
            OtDataField("GlyphID", "Start", description="First GlyphID in the range"),
            OtDataField("GlyphID", "End", description="Last GlyphID in the range"),
            OtDataField(
                "uint16",
                "StartCoverageIndex",
                description="Coverage Index of first GlyphID in range",
            ),
        ],
    ),
    (
        "ClassDefFormat1",
        [
            OtDataField(
                "uint16", "ClassFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "GlyphID",
                "StartGlyph",
                description="First GlyphID of the ClassValueArray",
            ),
            OtDataField(
                "uint16", "GlyphCount", description="Size of the ClassValueArray"
            ),
            OtDataField(
                "uint16",
                "ClassValueArray",
                repeat="GlyphCount",
                aux=0,
                description="Array of Class Values-one per GlyphID",
            ),
        ],
    ),
    (
        "ClassDefFormat2",
        [
            OtDataField(
                "uint16", "ClassFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "uint16", "ClassRangeCount", description="Number of ClassRangeRecords"
            ),
            OtDataField(
                "struct",
                "ClassRangeRecord",
                repeat="ClassRangeCount",
                aux=0,
                description="Array of ClassRangeRecords-ordered by Start GlyphID",
            ),
        ],
    ),
    (
        "ClassRangeRecord",
        [
            OtDataField("GlyphID", "Start", description="First GlyphID in the range"),
            OtDataField("GlyphID", "End", description="Last GlyphID in the range"),
            OtDataField(
                "uint16", "Class", description="Applied to all glyphs in the range"
            ),
        ],
    ),
    (
        "Device",
        [
            OtDataField(
                "uint16", "StartSize", description="Smallest size to correct-in ppem"
            ),
            OtDataField(
                "uint16", "EndSize", description="Largest size to correct-in ppem"
            ),
            OtDataField(
                "uint16",
                "DeltaFormat",
                description="Format of DeltaValue array data: 1, 2, or 3",
            ),
            OtDataField(
                "DeltaValue",
                "DeltaValue",
                aux="DeltaFormat in (1,2,3)",
                description="Array of compressed data",
            ),
        ],
    ),
    #
    # gpos
    #
    (
        "GPOS",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the GPOS table- 0x00010000 or 0x00010001",
            ),
            OtDataField(
                "Offset",
                "ScriptList",
                description="Offset to ScriptList table-from beginning of GPOS table",
            ),
            OtDataField(
                "Offset",
                "FeatureList",
                description="Offset to FeatureList table-from beginning of GPOS table",
            ),
            OtDataField(
                "Offset",
                "LookupList",
                description="Offset to LookupList table-from beginning of GPOS table",
            ),
            OtDataField(
                "LOffset",
                "FeatureVariations",
                aux="Version >= 0x00010001",
                description="Offset to FeatureVariations table-from beginning of GPOS table",
            ),
        ],
    ),
    (
        "SinglePosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of SinglePos subtable",
            ),
            OtDataField(
                "uint16",
                "ValueFormat",
                description="Defines the types of data in the ValueRecord",
            ),
            OtDataField(
                "ValueRecord",
                "Value",
                description="Defines positioning value(s)-applied to all glyphs in the Coverage table",
            ),
        ],
    ),
    (
        "SinglePosFormat2",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of SinglePos subtable",
            ),
            OtDataField(
                "uint16",
                "ValueFormat",
                description="Defines the types of data in the ValueRecord",
            ),
            OtDataField("uint16", "ValueCount", description="Number of ValueRecords"),
            OtDataField(
                "ValueRecord",
                "Value",
                repeat="ValueCount",
                aux=0,
                description="Array of ValueRecords-positioning values applied to glyphs",
            ),
        ],
    ),
    (
        "PairPosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of PairPos subtable-only the first glyph in each pair",
            ),
            OtDataField(
                "uint16",
                "ValueFormat1",
                description="Defines the types of data in ValueRecord1-for the first glyph in the pair -may be zero (0)",
            ),
            OtDataField(
                "uint16",
                "ValueFormat2",
                description="Defines the types of data in ValueRecord2-for the second glyph in the pair -may be zero (0)",
            ),
            OtDataField(
                "uint16", "PairSetCount", description="Number of PairSet tables"
            ),
            OtDataField(
                "Offset",
                "PairSet",
                repeat="PairSetCount",
                aux=0,
                description="Array of offsets to PairSet tables-from beginning of PairPos subtable-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "PairSet",
        [
            OtDataField(
                "uint16", "PairValueCount", description="Number of PairValueRecords"
            ),
            OtDataField(
                "struct",
                "PairValueRecord",
                repeat="PairValueCount",
                aux=0,
                description="Array of PairValueRecords-ordered by GlyphID of the second glyph",
            ),
        ],
    ),
    (
        "PairValueRecord",
        [
            OtDataField(
                "GlyphID",
                "SecondGlyph",
                description="GlyphID of second glyph in the pair-first glyph is listed in the Coverage table",
            ),
            OtDataField(
                "ValueRecord",
                "Value1",
                description="Positioning data for the first glyph in the pair",
            ),
            OtDataField(
                "ValueRecord",
                "Value2",
                description="Positioning data for the second glyph in the pair",
            ),
        ],
    ),
    (
        "PairPosFormat2",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of PairPos subtable-for the first glyph of the pair",
            ),
            OtDataField(
                "uint16",
                "ValueFormat1",
                description="ValueRecord definition-for the first glyph of the pair-may be zero (0)",
            ),
            OtDataField(
                "uint16",
                "ValueFormat2",
                description="ValueRecord definition-for the second glyph of the pair-may be zero (0)",
            ),
            OtDataField(
                "Offset",
                "ClassDef1",
                description="Offset to ClassDef table-from beginning of PairPos subtable-for the first glyph of the pair",
            ),
            OtDataField(
                "Offset",
                "ClassDef2",
                description="Offset to ClassDef table-from beginning of PairPos subtable-for the second glyph of the pair",
            ),
            OtDataField(
                "uint16",
                "Class1Count",
                description="Number of classes in ClassDef1 table-includes Class0",
            ),
            OtDataField(
                "uint16",
                "Class2Count",
                description="Number of classes in ClassDef2 table-includes Class0",
            ),
            OtDataField(
                "struct",
                "Class1Record",
                repeat="Class1Count",
                aux=0,
                description="Array of Class1 records-ordered by Class1",
            ),
        ],
    ),
    (
        "Class1Record",
        [
            OtDataField(
                "struct",
                "Class2Record",
                repeat="Class2Count",
                aux=0,
                description="Array of Class2 records-ordered by Class2",
            ),
        ],
    ),
    (
        "Class2Record",
        [
            OtDataField(
                "ValueRecord",
                "Value1",
                description="Positioning for first glyph-empty if ValueFormat1 = 0",
            ),
            OtDataField(
                "ValueRecord",
                "Value2",
                description="Positioning for second glyph-empty if ValueFormat2 = 0",
            ),
        ],
    ),
    (
        "CursivePosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of CursivePos subtable",
            ),
            OtDataField(
                "uint16", "EntryExitCount", description="Number of EntryExit records"
            ),
            OtDataField(
                "struct",
                "EntryExitRecord",
                repeat="EntryExitCount",
                aux=0,
                description="Array of EntryExit records-in Coverage Index order",
            ),
        ],
    ),
    (
        "EntryExitRecord",
        [
            OtDataField(
                "Offset",
                "EntryAnchor",
                description="Offset to EntryAnchor table-from beginning of CursivePos subtable-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ExitAnchor",
                description="Offset to ExitAnchor table-from beginning of CursivePos subtable-may be NULL",
            ),
        ],
    ),
    (
        "MarkBasePosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "MarkCoverage",
                description="Offset to MarkCoverage table-from beginning of MarkBasePos subtable",
            ),
            OtDataField(
                "Offset",
                "BaseCoverage",
                description="Offset to BaseCoverage table-from beginning of MarkBasePos subtable",
            ),
            OtDataField(
                "uint16",
                "ClassCount",
                description="Number of classes defined for marks",
            ),
            OtDataField(
                "Offset",
                "MarkArray",
                description="Offset to MarkArray table-from beginning of MarkBasePos subtable",
            ),
            OtDataField(
                "Offset",
                "BaseArray",
                description="Offset to BaseArray table-from beginning of MarkBasePos subtable",
            ),
        ],
    ),
    (
        "BaseArray",
        [
            OtDataField("uint16", "BaseCount", description="Number of BaseRecords"),
            OtDataField(
                "struct",
                "BaseRecord",
                repeat="BaseCount",
                aux=0,
                description="Array of BaseRecords-in order of BaseCoverage Index",
            ),
        ],
    ),
    (
        "BaseRecord",
        [
            OtDataField(
                "Offset",
                "BaseAnchor",
                repeat="ClassCount",
                aux=0,
                description="Array of offsets (one per class) to Anchor tables-from beginning of BaseArray table-ordered by class-zero-based",
            ),
        ],
    ),
    (
        "MarkLigPosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "MarkCoverage",
                description="Offset to Mark Coverage table-from beginning of MarkLigPos subtable",
            ),
            OtDataField(
                "Offset",
                "LigatureCoverage",
                description="Offset to Ligature Coverage table-from beginning of MarkLigPos subtable",
            ),
            OtDataField(
                "uint16", "ClassCount", description="Number of defined mark classes"
            ),
            OtDataField(
                "Offset",
                "MarkArray",
                description="Offset to MarkArray table-from beginning of MarkLigPos subtable",
            ),
            OtDataField(
                "Offset",
                "LigatureArray",
                description="Offset to LigatureArray table-from beginning of MarkLigPos subtable",
            ),
        ],
    ),
    (
        "LigatureArray",
        [
            OtDataField(
                "uint16",
                "LigatureCount",
                description="Number of LigatureAttach table offsets",
            ),
            OtDataField(
                "Offset",
                "LigatureAttach",
                repeat="LigatureCount",
                aux=0,
                description="Array of offsets to LigatureAttach tables-from beginning of LigatureArray table-ordered by LigatureCoverage Index",
            ),
        ],
    ),
    (
        "LigatureAttach",
        [
            OtDataField(
                "uint16",
                "ComponentCount",
                description="Number of ComponentRecords in this ligature",
            ),
            OtDataField(
                "struct",
                "ComponentRecord",
                repeat="ComponentCount",
                aux=0,
                description="Array of Component records-ordered in writing direction",
            ),
        ],
    ),
    (
        "ComponentRecord",
        [
            OtDataField(
                "Offset",
                "LigatureAnchor",
                repeat="ClassCount",
                aux=0,
                description="Array of offsets (one per class) to Anchor tables-from beginning of LigatureAttach table-ordered by class-NULL if a component does not have an attachment for a class-zero-based array",
            ),
        ],
    ),
    (
        "MarkMarkPosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Mark1Coverage",
                description="Offset to Combining Mark Coverage table-from beginning of MarkMarkPos subtable",
            ),
            OtDataField(
                "Offset",
                "Mark2Coverage",
                description="Offset to Base Mark Coverage table-from beginning of MarkMarkPos subtable",
            ),
            OtDataField(
                "uint16",
                "ClassCount",
                description="Number of Combining Mark classes defined",
            ),
            OtDataField(
                "Offset",
                "Mark1Array",
                description="Offset to MarkArray table for Mark1-from beginning of MarkMarkPos subtable",
            ),
            OtDataField(
                "Offset",
                "Mark2Array",
                description="Offset to Mark2Array table for Mark2-from beginning of MarkMarkPos subtable",
            ),
        ],
    ),
    (
        "Mark2Array",
        [
            OtDataField("uint16", "Mark2Count", description="Number of Mark2 records"),
            OtDataField(
                "struct",
                "Mark2Record",
                repeat="Mark2Count",
                aux=0,
                description="Array of Mark2 records-in Coverage order",
            ),
        ],
    ),
    (
        "Mark2Record",
        [
            OtDataField(
                "Offset",
                "Mark2Anchor",
                repeat="ClassCount",
                aux=0,
                description="Array of offsets (one per class) to Anchor tables-from beginning of Mark2Array table-zero-based array",
            ),
        ],
    ),
    (
        "PosLookupRecord",
        [
            OtDataField(
                "uint16",
                "SequenceIndex",
                description="Index to input glyph sequence-first glyph = 0",
            ),
            OtDataField(
                "uint16",
                "LookupListIndex",
                description="Lookup to apply to that position-zero-based",
            ),
        ],
    ),
    (
        "ContextPosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of ContextPos subtable",
            ),
            OtDataField(
                "uint16", "PosRuleSetCount", description="Number of PosRuleSet tables"
            ),
            OtDataField(
                "Offset",
                "PosRuleSet",
                repeat="PosRuleSetCount",
                aux=0,
                description="Array of offsets to PosRuleSet tables-from beginning of ContextPos subtable-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "PosRuleSet",
        [
            OtDataField(
                "uint16", "PosRuleCount", description="Number of PosRule tables"
            ),
            OtDataField(
                "Offset",
                "PosRule",
                repeat="PosRuleCount",
                aux=0,
                description="Array of offsets to PosRule tables-from beginning of PosRuleSet-ordered by preference",
            ),
        ],
    ),
    (
        "PosRule",
        [
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of glyphs in the Input glyph sequence",
            ),
            OtDataField("uint16", "PosCount", description="Number of PosLookupRecords"),
            OtDataField(
                "GlyphID",
                "Input",
                repeat="GlyphCount",
                aux=-1,
                description="Array of input GlyphIDs-starting with the second glyph",
            ),
            OtDataField(
                "struct",
                "PosLookupRecord",
                repeat="PosCount",
                aux=0,
                description="Array of positioning lookups-in design order",
            ),
        ],
    ),
    (
        "ContextPosFormat2",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of ContextPos subtable",
            ),
            OtDataField(
                "Offset",
                "ClassDef",
                description="Offset to ClassDef table-from beginning of ContextPos subtable",
            ),
            OtDataField(
                "uint16", "PosClassSetCount", description="Number of PosClassSet tables"
            ),
            OtDataField(
                "Offset",
                "PosClassSet",
                repeat="PosClassSetCount",
                aux=0,
                description="Array of offsets to PosClassSet tables-from beginning of ContextPos subtable-ordered by class-may be NULL",
            ),
        ],
    ),
    (
        "PosClassSet",
        [
            OtDataField(
                "uint16",
                "PosClassRuleCount",
                description="Number of PosClassRule tables",
            ),
            OtDataField(
                "Offset",
                "PosClassRule",
                repeat="PosClassRuleCount",
                aux=0,
                description="Array of offsets to PosClassRule tables-from beginning of PosClassSet-ordered by preference",
            ),
        ],
    ),
    (
        "PosClassRule",
        [
            OtDataField(
                "uint16", "GlyphCount", description="Number of glyphs to be matched"
            ),
            OtDataField("uint16", "PosCount", description="Number of PosLookupRecords"),
            OtDataField(
                "uint16",
                "Class",
                repeat="GlyphCount",
                aux=-1,
                description="Array of classes-beginning with the second class-to be matched to the input glyph sequence",
            ),
            OtDataField(
                "struct",
                "PosLookupRecord",
                repeat="PosCount",
                aux=0,
                description="Array of positioning lookups-in design order",
            ),
        ],
    ),
    (
        "ContextPosFormat3",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of glyphs in the input sequence",
            ),
            OtDataField("uint16", "PosCount", description="Number of PosLookupRecords"),
            OtDataField(
                "Offset",
                "Coverage",
                repeat="GlyphCount",
                aux=0,
                description="Array of offsets to Coverage tables-from beginning of ContextPos subtable",
            ),
            OtDataField(
                "struct",
                "PosLookupRecord",
                repeat="PosCount",
                aux=0,
                description="Array of positioning lookups-in design order",
            ),
        ],
    ),
    (
        "ChainContextPosFormat1",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of ContextPos subtable",
            ),
            OtDataField(
                "uint16",
                "ChainPosRuleSetCount",
                description="Number of ChainPosRuleSet tables",
            ),
            OtDataField(
                "Offset",
                "ChainPosRuleSet",
                repeat="ChainPosRuleSetCount",
                aux=0,
                description="Array of offsets to ChainPosRuleSet tables-from beginning of ContextPos subtable-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "ChainPosRuleSet",
        [
            OtDataField(
                "uint16",
                "ChainPosRuleCount",
                description="Number of ChainPosRule tables",
            ),
            OtDataField(
                "Offset",
                "ChainPosRule",
                repeat="ChainPosRuleCount",
                aux=0,
                description="Array of offsets to ChainPosRule tables-from beginning of ChainPosRuleSet-ordered by preference",
            ),
        ],
    ),
    (
        "ChainPosRule",
        [
            OtDataField(
                "uint16",
                "BacktrackGlyphCount",
                description="Total number of glyphs in the backtrack sequence (number of glyphs to be matched before the first glyph)",
            ),
            OtDataField(
                "GlyphID",
                "Backtrack",
                repeat="BacktrackGlyphCount",
                aux=0,
                description="Array of backtracking GlyphID's (to be matched before the input sequence)",
            ),
            OtDataField(
                "uint16",
                "InputGlyphCount",
                description="Total number of glyphs in the input sequence (includes the first glyph)",
            ),
            OtDataField(
                "GlyphID",
                "Input",
                repeat="InputGlyphCount",
                aux=-1,
                description="Array of input GlyphIDs (start with second glyph)",
            ),
            OtDataField(
                "uint16",
                "LookAheadGlyphCount",
                description="Total number of glyphs in the look ahead sequence (number of glyphs to be matched after the input sequence)",
            ),
            OtDataField(
                "GlyphID",
                "LookAhead",
                repeat="LookAheadGlyphCount",
                aux=0,
                description="Array of lookahead GlyphID's (to be matched after the input sequence)",
            ),
            OtDataField("uint16", "PosCount", description="Number of PosLookupRecords"),
            OtDataField(
                "struct",
                "PosLookupRecord",
                repeat="PosCount",
                aux=0,
                description="Array of PosLookupRecords (in design order)",
            ),
        ],
    ),
    (
        "ChainContextPosFormat2",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of ChainContextPos subtable",
            ),
            OtDataField(
                "Offset",
                "BacktrackClassDef",
                description="Offset to ClassDef table containing backtrack sequence context-from beginning of ChainContextPos subtable",
            ),
            OtDataField(
                "Offset",
                "InputClassDef",
                description="Offset to ClassDef table containing input sequence context-from beginning of ChainContextPos subtable",
            ),
            OtDataField(
                "Offset",
                "LookAheadClassDef",
                description="Offset to ClassDef table containing lookahead sequence context-from beginning of ChainContextPos subtable",
            ),
            OtDataField(
                "uint16",
                "ChainPosClassSetCount",
                description="Number of ChainPosClassSet tables",
            ),
            OtDataField(
                "Offset",
                "ChainPosClassSet",
                repeat="ChainPosClassSetCount",
                aux=0,
                description="Array of offsets to ChainPosClassSet tables-from beginning of ChainContextPos subtable-ordered by input class-may be NULL",
            ),
        ],
    ),
    (
        "ChainPosClassSet",
        [
            OtDataField(
                "uint16",
                "ChainPosClassRuleCount",
                description="Number of ChainPosClassRule tables",
            ),
            OtDataField(
                "Offset",
                "ChainPosClassRule",
                repeat="ChainPosClassRuleCount",
                aux=0,
                description="Array of offsets to ChainPosClassRule tables-from beginning of ChainPosClassSet-ordered by preference",
            ),
        ],
    ),
    (
        "ChainPosClassRule",
        [
            OtDataField(
                "uint16",
                "BacktrackGlyphCount",
                description="Total number of glyphs in the backtrack sequence (number of glyphs to be matched before the first glyph)",
            ),
            OtDataField(
                "uint16",
                "Backtrack",
                repeat="BacktrackGlyphCount",
                aux=0,
                description="Array of backtracking classes(to be matched before the input sequence)",
            ),
            OtDataField(
                "uint16",
                "InputGlyphCount",
                description="Total number of classes in the input sequence (includes the first class)",
            ),
            OtDataField(
                "uint16",
                "Input",
                repeat="InputGlyphCount",
                aux=-1,
                description="Array of input classes(start with second class; to be matched with the input glyph sequence)",
            ),
            OtDataField(
                "uint16",
                "LookAheadGlyphCount",
                description="Total number of classes in the look ahead sequence (number of classes to be matched after the input sequence)",
            ),
            OtDataField(
                "uint16",
                "LookAhead",
                repeat="LookAheadGlyphCount",
                aux=0,
                description="Array of lookahead classes(to be matched after the input sequence)",
            ),
            OtDataField("uint16", "PosCount", description="Number of PosLookupRecords"),
            OtDataField(
                "struct",
                "PosLookupRecord",
                repeat="PosCount",
                aux=0,
                description="Array of PosLookupRecords (in design order)",
            ),
        ],
    ),
    (
        "ChainContextPosFormat3",
        [
            OtDataField(
                "uint16", "PosFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "uint16",
                "BacktrackGlyphCount",
                description="Number of glyphs in the backtracking sequence",
            ),
            OtDataField(
                "Offset",
                "BacktrackCoverage",
                repeat="BacktrackGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in backtracking sequence, in glyph sequence order",
            ),
            OtDataField(
                "uint16",
                "InputGlyphCount",
                description="Number of glyphs in input sequence",
            ),
            OtDataField(
                "Offset",
                "InputCoverage",
                repeat="InputGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in input sequence, in glyph sequence order",
            ),
            OtDataField(
                "uint16",
                "LookAheadGlyphCount",
                description="Number of glyphs in lookahead sequence",
            ),
            OtDataField(
                "Offset",
                "LookAheadCoverage",
                repeat="LookAheadGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in lookahead sequence, in glyph sequence order",
            ),
            OtDataField("uint16", "PosCount", description="Number of PosLookupRecords"),
            OtDataField(
                "struct",
                "PosLookupRecord",
                repeat="PosCount",
                aux=0,
                description="Array of PosLookupRecords,in design order",
            ),
        ],
    ),
    (
        "ExtensionPosFormat1",
        [
            OtDataField(
                "uint16", "ExtFormat", description="Format identifier. Set to 1."
            ),
            OtDataField(
                "uint16",
                "ExtensionLookupType",
                description="Lookup type of subtable referenced by ExtensionOffset (i.e. the extension subtable).",
            ),
            OtDataField("LOffset", "ExtSubTable", description="Offset to SubTable"),
        ],
    ),
    # 	('ValueRecord', [
    # 		('int16', 'XPlacement', None, None, 'Horizontal adjustment for placement-in design units'),
    # 		('int16', 'YPlacement', None, None, 'Vertical adjustment for placement-in design units'),
    # 		('int16', 'XAdvance', None, None, 'Horizontal adjustment for advance-in design units (only used for horizontal writing)'),
    # 		('int16', 'YAdvance', None, None, 'Vertical adjustment for advance-in design units (only used for vertical writing)'),
    # 		('Offset', 'XPlaDevice', None, None, 'Offset to Device table for horizontal placement-measured from beginning of PosTable (may be NULL)'),
    # 		('Offset', 'YPlaDevice', None, None, 'Offset to Device table for vertical placement-measured from beginning of PosTable (may be NULL)'),
    # 		('Offset', 'XAdvDevice', None, None, 'Offset to Device table for horizontal advance-measured from beginning of PosTable (may be NULL)'),
    # 		('Offset', 'YAdvDevice', None, None, 'Offset to Device table for vertical advance-measured from beginning of PosTable (may be NULL)'),
    # 	]),
    (
        "AnchorFormat1",
        [
            OtDataField(
                "uint16", "AnchorFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "int16", "XCoordinate", description="Horizontal value-in design units"
            ),
            OtDataField(
                "int16", "YCoordinate", description="Vertical value-in design units"
            ),
        ],
    ),
    (
        "AnchorFormat2",
        [
            OtDataField(
                "uint16", "AnchorFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "int16", "XCoordinate", description="Horizontal value-in design units"
            ),
            OtDataField(
                "int16", "YCoordinate", description="Vertical value-in design units"
            ),
            OtDataField(
                "uint16", "AnchorPoint", description="Index to glyph contour point"
            ),
        ],
    ),
    (
        "AnchorFormat3",
        [
            OtDataField(
                "uint16", "AnchorFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "int16", "XCoordinate", description="Horizontal value-in design units"
            ),
            OtDataField(
                "int16", "YCoordinate", description="Vertical value-in design units"
            ),
            OtDataField(
                "Offset",
                "XDeviceTable",
                description="Offset to Device table for X coordinate- from beginning of Anchor table (may be NULL)",
            ),
            OtDataField(
                "Offset",
                "YDeviceTable",
                description="Offset to Device table for Y coordinate- from beginning of Anchor table (may be NULL)",
            ),
        ],
    ),
    (
        "MarkArray",
        [
            OtDataField("uint16", "MarkCount", description="Number of MarkRecords"),
            OtDataField(
                "struct",
                "MarkRecord",
                repeat="MarkCount",
                aux=0,
                description="Array of MarkRecords-in Coverage order",
            ),
        ],
    ),
    (
        "MarkRecord",
        [
            OtDataField("uint16", "Class", description="Class defined for this mark"),
            OtDataField(
                "Offset",
                "MarkAnchor",
                description="Offset to Anchor table-from beginning of MarkArray table",
            ),
        ],
    ),
    #
    # gsub
    #
    (
        "GSUB",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the GSUB table- 0x00010000 or 0x00010001",
            ),
            OtDataField(
                "Offset",
                "ScriptList",
                description="Offset to ScriptList table-from beginning of GSUB table",
            ),
            OtDataField(
                "Offset",
                "FeatureList",
                description="Offset to FeatureList table-from beginning of GSUB table",
            ),
            OtDataField(
                "Offset",
                "LookupList",
                description="Offset to LookupList table-from beginning of GSUB table",
            ),
            OtDataField(
                "LOffset",
                "FeatureVariations",
                aux="Version >= 0x00010001",
                description="Offset to FeatureVariations table-from beginning of GSUB table",
            ),
        ],
    ),
    (
        "SingleSubstFormat1",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "DeltaGlyphID",
                description="Add to original GlyphID modulo 65536 to get substitute GlyphID",
            ),
        ],
    ),
    (
        "SingleSubstFormat2",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of GlyphIDs in the Substitute array",
            ),
            OtDataField(
                "GlyphID",
                "Substitute",
                repeat="GlyphCount",
                aux=0,
                description="Array of substitute GlyphIDs-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "MultipleSubstFormat1",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "SequenceCount",
                description="Number of Sequence table offsets in the Sequence array",
            ),
            OtDataField(
                "Offset",
                "Sequence",
                repeat="SequenceCount",
                aux=0,
                description="Array of offsets to Sequence tables-from beginning of Substitution table-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "Sequence",
        [
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of GlyphIDs in the Substitute array. This should always be greater than 0.",
            ),
            OtDataField(
                "GlyphID",
                "Substitute",
                repeat="GlyphCount",
                aux=0,
                description="String of GlyphIDs to substitute",
            ),
        ],
    ),
    (
        "AlternateSubstFormat1",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "AlternateSetCount",
                description="Number of AlternateSet tables",
            ),
            OtDataField(
                "Offset",
                "AlternateSet",
                repeat="AlternateSetCount",
                aux=0,
                description="Array of offsets to AlternateSet tables-from beginning of Substitution table-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "AlternateSet",
        [
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of GlyphIDs in the Alternate array",
            ),
            OtDataField(
                "GlyphID",
                "Alternate",
                repeat="GlyphCount",
                aux=0,
                description="Array of alternate GlyphIDs-in arbitrary order",
            ),
        ],
    ),
    (
        "LigatureSubstFormat1",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16", "LigSetCount", description="Number of LigatureSet tables"
            ),
            OtDataField(
                "Offset",
                "LigatureSet",
                repeat="LigSetCount",
                aux=0,
                description="Array of offsets to LigatureSet tables-from beginning of Substitution table-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "LigatureSet",
        [
            OtDataField(
                "uint16", "LigatureCount", description="Number of Ligature tables"
            ),
            OtDataField(
                "Offset",
                "Ligature",
                repeat="LigatureCount",
                aux=0,
                description="Array of offsets to Ligature tables-from beginning of LigatureSet table-ordered by preference",
            ),
        ],
    ),
    (
        "Ligature",
        [
            OtDataField(
                "GlyphID", "LigGlyph", description="GlyphID of ligature to substitute"
            ),
            OtDataField(
                "uint16",
                "CompCount",
                description="Number of components in the ligature",
            ),
            OtDataField(
                "GlyphID",
                "Component",
                repeat="CompCount",
                aux=-1,
                description="Array of component GlyphIDs-start with the second component-ordered in writing direction",
            ),
        ],
    ),
    (
        "SubstLookupRecord",
        [
            OtDataField(
                "uint16",
                "SequenceIndex",
                description="Index into current glyph sequence-first glyph = 0",
            ),
            OtDataField(
                "uint16",
                "LookupListIndex",
                description="Lookup to apply to that position-zero-based",
            ),
        ],
    ),
    (
        "ContextSubstFormat1",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "SubRuleSetCount",
                description="Number of SubRuleSet tables-must equal GlyphCount in Coverage table",
            ),
            OtDataField(
                "Offset",
                "SubRuleSet",
                repeat="SubRuleSetCount",
                aux=0,
                description="Array of offsets to SubRuleSet tables-from beginning of Substitution table-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "SubRuleSet",
        [
            OtDataField(
                "uint16", "SubRuleCount", description="Number of SubRule tables"
            ),
            OtDataField(
                "Offset",
                "SubRule",
                repeat="SubRuleCount",
                aux=0,
                description="Array of offsets to SubRule tables-from beginning of SubRuleSet table-ordered by preference",
            ),
        ],
    ),
    (
        "SubRule",
        [
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Total number of glyphs in input glyph sequence-includes the first glyph",
            ),
            OtDataField(
                "uint16", "SubstCount", description="Number of SubstLookupRecords"
            ),
            OtDataField(
                "GlyphID",
                "Input",
                repeat="GlyphCount",
                aux=-1,
                description="Array of input GlyphIDs-start with second glyph",
            ),
            OtDataField(
                "struct",
                "SubstLookupRecord",
                repeat="SubstCount",
                aux=0,
                description="Array of SubstLookupRecords-in design order",
            ),
        ],
    ),
    (
        "ContextSubstFormat2",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "Offset",
                "ClassDef",
                description="Offset to glyph ClassDef table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16", "SubClassSetCount", description="Number of SubClassSet tables"
            ),
            OtDataField(
                "Offset",
                "SubClassSet",
                repeat="SubClassSetCount",
                aux=0,
                description="Array of offsets to SubClassSet tables-from beginning of Substitution table-ordered by class-may be NULL",
            ),
        ],
    ),
    (
        "SubClassSet",
        [
            OtDataField(
                "uint16",
                "SubClassRuleCount",
                description="Number of SubClassRule tables",
            ),
            OtDataField(
                "Offset",
                "SubClassRule",
                repeat="SubClassRuleCount",
                aux=0,
                description="Array of offsets to SubClassRule tables-from beginning of SubClassSet-ordered by preference",
            ),
        ],
    ),
    (
        "SubClassRule",
        [
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Total number of classes specified for the context in the rule-includes the first class",
            ),
            OtDataField(
                "uint16", "SubstCount", description="Number of SubstLookupRecords"
            ),
            OtDataField(
                "uint16",
                "Class",
                repeat="GlyphCount",
                aux=-1,
                description="Array of classes-beginning with the second class-to be matched to the input glyph class sequence",
            ),
            OtDataField(
                "struct",
                "SubstLookupRecord",
                repeat="SubstCount",
                aux=0,
                description="Array of Substitution lookups-in design order",
            ),
        ],
    ),
    (
        "ContextSubstFormat3",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of glyphs in the input glyph sequence",
            ),
            OtDataField(
                "uint16", "SubstCount", description="Number of SubstLookupRecords"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                repeat="GlyphCount",
                aux=0,
                description="Array of offsets to Coverage table-from beginning of Substitution table-in glyph sequence order",
            ),
            OtDataField(
                "struct",
                "SubstLookupRecord",
                repeat="SubstCount",
                aux=0,
                description="Array of SubstLookupRecords-in design order",
            ),
        ],
    ),
    (
        "ChainContextSubstFormat1",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "ChainSubRuleSetCount",
                description="Number of ChainSubRuleSet tables-must equal GlyphCount in Coverage table",
            ),
            OtDataField(
                "Offset",
                "ChainSubRuleSet",
                repeat="ChainSubRuleSetCount",
                aux=0,
                description="Array of offsets to ChainSubRuleSet tables-from beginning of Substitution table-ordered by Coverage Index",
            ),
        ],
    ),
    (
        "ChainSubRuleSet",
        [
            OtDataField(
                "uint16",
                "ChainSubRuleCount",
                description="Number of ChainSubRule tables",
            ),
            OtDataField(
                "Offset",
                "ChainSubRule",
                repeat="ChainSubRuleCount",
                aux=0,
                description="Array of offsets to ChainSubRule tables-from beginning of ChainSubRuleSet table-ordered by preference",
            ),
        ],
    ),
    (
        "ChainSubRule",
        [
            OtDataField(
                "uint16",
                "BacktrackGlyphCount",
                description="Total number of glyphs in the backtrack sequence (number of glyphs to be matched before the first glyph)",
            ),
            OtDataField(
                "GlyphID",
                "Backtrack",
                repeat="BacktrackGlyphCount",
                aux=0,
                description="Array of backtracking GlyphID's (to be matched before the input sequence)",
            ),
            OtDataField(
                "uint16",
                "InputGlyphCount",
                description="Total number of glyphs in the input sequence (includes the first glyph)",
            ),
            OtDataField(
                "GlyphID",
                "Input",
                repeat="InputGlyphCount",
                aux=-1,
                description="Array of input GlyphIDs (start with second glyph)",
            ),
            OtDataField(
                "uint16",
                "LookAheadGlyphCount",
                description="Total number of glyphs in the look ahead sequence (number of glyphs to be matched after the input sequence)",
            ),
            OtDataField(
                "GlyphID",
                "LookAhead",
                repeat="LookAheadGlyphCount",
                aux=0,
                description="Array of lookahead GlyphID's (to be matched after the input sequence)",
            ),
            OtDataField(
                "uint16", "SubstCount", description="Number of SubstLookupRecords"
            ),
            OtDataField(
                "struct",
                "SubstLookupRecord",
                repeat="SubstCount",
                aux=0,
                description="Array of SubstLookupRecords (in design order)",
            ),
        ],
    ),
    (
        "ChainContextSubstFormat2",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table-from beginning of Substitution table",
            ),
            OtDataField(
                "Offset",
                "BacktrackClassDef",
                description="Offset to glyph ClassDef table containing backtrack sequence data-from beginning of Substitution table",
            ),
            OtDataField(
                "Offset",
                "InputClassDef",
                description="Offset to glyph ClassDef table containing input sequence data-from beginning of Substitution table",
            ),
            OtDataField(
                "Offset",
                "LookAheadClassDef",
                description="Offset to glyph ClassDef table containing lookahead sequence data-from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "ChainSubClassSetCount",
                description="Number of ChainSubClassSet tables",
            ),
            OtDataField(
                "Offset",
                "ChainSubClassSet",
                repeat="ChainSubClassSetCount",
                aux=0,
                description="Array of offsets to ChainSubClassSet tables-from beginning of Substitution table-ordered by input class-may be NULL",
            ),
        ],
    ),
    (
        "ChainSubClassSet",
        [
            OtDataField(
                "uint16",
                "ChainSubClassRuleCount",
                description="Number of ChainSubClassRule tables",
            ),
            OtDataField(
                "Offset",
                "ChainSubClassRule",
                repeat="ChainSubClassRuleCount",
                aux=0,
                description="Array of offsets to ChainSubClassRule tables-from beginning of ChainSubClassSet-ordered by preference",
            ),
        ],
    ),
    (
        "ChainSubClassRule",
        [
            OtDataField(
                "uint16",
                "BacktrackGlyphCount",
                description="Total number of glyphs in the backtrack sequence (number of glyphs to be matched before the first glyph)",
            ),
            OtDataField(
                "uint16",
                "Backtrack",
                repeat="BacktrackGlyphCount",
                aux=0,
                description="Array of backtracking classes(to be matched before the input sequence)",
            ),
            OtDataField(
                "uint16",
                "InputGlyphCount",
                description="Total number of classes in the input sequence (includes the first class)",
            ),
            OtDataField(
                "uint16",
                "Input",
                repeat="InputGlyphCount",
                aux=-1,
                description="Array of input classes(start with second class; to be matched with the input glyph sequence)",
            ),
            OtDataField(
                "uint16",
                "LookAheadGlyphCount",
                description="Total number of classes in the look ahead sequence (number of classes to be matched after the input sequence)",
            ),
            OtDataField(
                "uint16",
                "LookAhead",
                repeat="LookAheadGlyphCount",
                aux=0,
                description="Array of lookahead classes(to be matched after the input sequence)",
            ),
            OtDataField(
                "uint16", "SubstCount", description="Number of SubstLookupRecords"
            ),
            OtDataField(
                "struct",
                "SubstLookupRecord",
                repeat="SubstCount",
                aux=0,
                description="Array of SubstLookupRecords (in design order)",
            ),
        ],
    ),
    (
        "ChainContextSubstFormat3",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "uint16",
                "BacktrackGlyphCount",
                description="Number of glyphs in the backtracking sequence",
            ),
            OtDataField(
                "Offset",
                "BacktrackCoverage",
                repeat="BacktrackGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in backtracking sequence, in glyph sequence order",
            ),
            OtDataField(
                "uint16",
                "InputGlyphCount",
                description="Number of glyphs in input sequence",
            ),
            OtDataField(
                "Offset",
                "InputCoverage",
                repeat="InputGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in input sequence, in glyph sequence order",
            ),
            OtDataField(
                "uint16",
                "LookAheadGlyphCount",
                description="Number of glyphs in lookahead sequence",
            ),
            OtDataField(
                "Offset",
                "LookAheadCoverage",
                repeat="LookAheadGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in lookahead sequence, in glyph sequence order",
            ),
            OtDataField(
                "uint16", "SubstCount", description="Number of SubstLookupRecords"
            ),
            OtDataField(
                "struct",
                "SubstLookupRecord",
                repeat="SubstCount",
                aux=0,
                description="Array of SubstLookupRecords, in design order",
            ),
        ],
    ),
    (
        "ExtensionSubstFormat1",
        [
            OtDataField(
                "uint16", "ExtFormat", description="Format identifier. Set to 1."
            ),
            OtDataField(
                "uint16",
                "ExtensionLookupType",
                description="Lookup type of subtable referenced by ExtensionOffset (i.e. the extension subtable).",
            ),
            OtDataField(
                "LOffset",
                "ExtSubTable",
                description="Array of offsets to Lookup tables-from beginning of LookupList -zero based (first lookup is Lookup index = 0)",
            ),
        ],
    ),
    (
        "ReverseChainSingleSubstFormat1",
        [
            OtDataField(
                "uint16", "SubstFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "Offset",
                "Coverage",
                aux=0,
                description="Offset to Coverage table - from beginning of Substitution table",
            ),
            OtDataField(
                "uint16",
                "BacktrackGlyphCount",
                description="Number of glyphs in the backtracking sequence",
            ),
            OtDataField(
                "Offset",
                "BacktrackCoverage",
                repeat="BacktrackGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in backtracking sequence, in glyph sequence order",
            ),
            OtDataField(
                "uint16",
                "LookAheadGlyphCount",
                description="Number of glyphs in lookahead sequence",
            ),
            OtDataField(
                "Offset",
                "LookAheadCoverage",
                repeat="LookAheadGlyphCount",
                aux=0,
                description="Array of offsets to coverage tables in lookahead sequence, in glyph sequence order",
            ),
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of GlyphIDs in the Substitute array",
            ),
            OtDataField(
                "GlyphID",
                "Substitute",
                repeat="GlyphCount",
                aux=0,
                description="Array of substitute GlyphIDs-ordered by Coverage index",
            ),
        ],
    ),
    #
    # gdef
    #
    (
        "GDEF",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the GDEF table- 0x00010000, 0x00010002, or 0x00010003",
            ),
            OtDataField(
                "Offset",
                "GlyphClassDef",
                description="Offset to class definition table for glyph type-from beginning of GDEF header (may be NULL)",
            ),
            OtDataField(
                "Offset",
                "AttachList",
                description="Offset to list of glyphs with attachment points-from beginning of GDEF header (may be NULL)",
            ),
            OtDataField(
                "Offset",
                "LigCaretList",
                description="Offset to list of positioning points for ligature carets-from beginning of GDEF header (may be NULL)",
            ),
            OtDataField(
                "Offset",
                "MarkAttachClassDef",
                description="Offset to class definition table for mark attachment type-from beginning of GDEF header (may be NULL)",
            ),
            OtDataField(
                "Offset",
                "MarkGlyphSetsDef",
                aux="Version >= 0x00010002",
                description="Offset to the table of mark set definitions-from beginning of GDEF header (may be NULL)",
            ),
            OtDataField(
                "LOffset",
                "VarStore",
                aux="Version >= 0x00010003",
                description="Offset to variation store (may be NULL)",
            ),
        ],
    ),
    (
        "AttachList",
        [
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table - from beginning of AttachList table",
            ),
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of glyphs with attachment points",
            ),
            OtDataField(
                "Offset",
                "AttachPoint",
                repeat="GlyphCount",
                aux=0,
                description="Array of offsets to AttachPoint tables-from beginning of AttachList table-in Coverage Index order",
            ),
        ],
    ),
    (
        "AttachPoint",
        [
            OtDataField(
                "uint16",
                "PointCount",
                description="Number of attachment points on this glyph",
            ),
            OtDataField(
                "uint16",
                "PointIndex",
                repeat="PointCount",
                aux=0,
                description="Array of contour point indices -in increasing numerical order",
            ),
        ],
    ),
    (
        "LigCaretList",
        [
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table - from beginning of LigCaretList table",
            ),
            OtDataField(
                "uint16", "LigGlyphCount", description="Number of ligature glyphs"
            ),
            OtDataField(
                "Offset",
                "LigGlyph",
                repeat="LigGlyphCount",
                aux=0,
                description="Array of offsets to LigGlyph tables-from beginning of LigCaretList table-in Coverage Index order",
            ),
        ],
    ),
    (
        "LigGlyph",
        [
            OtDataField(
                "uint16",
                "CaretCount",
                description="Number of CaretValues for this ligature (components - 1)",
            ),
            OtDataField(
                "Offset",
                "CaretValue",
                repeat="CaretCount",
                aux=0,
                description="Array of offsets to CaretValue tables-from beginning of LigGlyph table-in increasing coordinate order",
            ),
        ],
    ),
    (
        "CaretValueFormat1",
        [
            OtDataField(
                "uint16", "CaretValueFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "int16", "Coordinate", description="X or Y value, in design units"
            ),
        ],
    ),
    (
        "CaretValueFormat2",
        [
            OtDataField(
                "uint16", "CaretValueFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "uint16", "CaretValuePoint", description="Contour point index on glyph"
            ),
        ],
    ),
    (
        "CaretValueFormat3",
        [
            OtDataField(
                "uint16", "CaretValueFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "int16", "Coordinate", description="X or Y value, in design units"
            ),
            OtDataField(
                "Offset",
                "DeviceTable",
                description="Offset to Device table for X or Y value-from beginning of CaretValue table",
            ),
        ],
    ),
    (
        "MarkGlyphSetsDef",
        [
            OtDataField(
                "uint16", "MarkSetTableFormat", description="Format identifier == 1"
            ),
            OtDataField(
                "uint16", "MarkSetCount", description="Number of mark sets defined"
            ),
            OtDataField(
                "LOffset",
                "Coverage",
                repeat="MarkSetCount",
                aux=0,
                description="Array of offsets to mark set coverage tables.",
            ),
        ],
    ),
    #
    # base
    #
    (
        "BASE",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the BASE table-initially 0x00010000",
            ),
            OtDataField(
                "Offset",
                "HorizAxis",
                description="Offset to horizontal Axis table-from beginning of BASE table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "VertAxis",
                description="Offset to vertical Axis table-from beginning of BASE table-may be NULL",
            ),
            OtDataField(
                "LOffset",
                "VarStore",
                aux="Version >= 0x00010001",
                description="Offset to variation store (may be NULL)",
            ),
        ],
    ),
    (
        "Axis",
        [
            OtDataField(
                "Offset",
                "BaseTagList",
                description="Offset to BaseTagList table-from beginning of Axis table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "BaseScriptList",
                description="Offset to BaseScriptList table-from beginning of Axis table",
            ),
        ],
    ),
    (
        "BaseTagList",
        [
            OtDataField(
                "uint16",
                "BaseTagCount",
                description="Number of baseline identification tags in this text direction-may be zero (0)",
            ),
            OtDataField(
                "Tag",
                "BaselineTag",
                repeat="BaseTagCount",
                aux=0,
                description="Array of 4-byte baseline identification tags-must be in alphabetical order",
            ),
        ],
    ),
    (
        "BaseScriptList",
        [
            OtDataField(
                "uint16",
                "BaseScriptCount",
                description="Number of BaseScriptRecords defined",
            ),
            OtDataField(
                "struct",
                "BaseScriptRecord",
                repeat="BaseScriptCount",
                aux=0,
                description="Array of BaseScriptRecords-in alphabetical order by BaseScriptTag",
            ),
        ],
    ),
    (
        "BaseScriptRecord",
        [
            OtDataField(
                "Tag", "BaseScriptTag", description="4-byte script identification tag"
            ),
            OtDataField(
                "Offset",
                "BaseScript",
                description="Offset to BaseScript table-from beginning of BaseScriptList",
            ),
        ],
    ),
    (
        "BaseScript",
        [
            OtDataField(
                "Offset",
                "BaseValues",
                description="Offset to BaseValues table-from beginning of BaseScript table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "DefaultMinMax",
                description="Offset to MinMax table- from beginning of BaseScript table-may be NULL",
            ),
            OtDataField(
                "uint16",
                "BaseLangSysCount",
                description="Number of BaseLangSysRecords defined-may be zero (0)",
            ),
            OtDataField(
                "struct",
                "BaseLangSysRecord",
                repeat="BaseLangSysCount",
                aux=0,
                description="Array of BaseLangSysRecords-in alphabetical order by BaseLangSysTag",
            ),
        ],
    ),
    (
        "BaseLangSysRecord",
        [
            OtDataField(
                "Tag",
                "BaseLangSysTag",
                description="4-byte language system identification tag",
            ),
            OtDataField(
                "Offset",
                "MinMax",
                description="Offset to MinMax table-from beginning of BaseScript table",
            ),
        ],
    ),
    (
        "BaseValues",
        [
            OtDataField(
                "uint16",
                "DefaultIndex",
                description="Index number of default baseline for this script-equals index position of baseline tag in BaselineArray of the BaseTagList",
            ),
            OtDataField(
                "uint16",
                "BaseCoordCount",
                description="Number of BaseCoord tables defined-should equal BaseTagCount in the BaseTagList",
            ),
            OtDataField(
                "Offset",
                "BaseCoord",
                repeat="BaseCoordCount",
                aux=0,
                description="Array of offsets to BaseCoord-from beginning of BaseValues table-order matches BaselineTag array in the BaseTagList",
            ),
        ],
    ),
    (
        "MinMax",
        [
            OtDataField(
                "Offset",
                "MinCoord",
                description="Offset to BaseCoord table-defines minimum extent value-from the beginning of MinMax table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "MaxCoord",
                description="Offset to BaseCoord table-defines maximum extent value-from the beginning of MinMax table-may be NULL",
            ),
            OtDataField(
                "uint16",
                "FeatMinMaxCount",
                description="Number of FeatMinMaxRecords-may be zero (0)",
            ),
            OtDataField(
                "struct",
                "FeatMinMaxRecord",
                repeat="FeatMinMaxCount",
                aux=0,
                description="Array of FeatMinMaxRecords-in alphabetical order, by FeatureTableTag",
            ),
        ],
    ),
    (
        "FeatMinMaxRecord",
        [
            OtDataField(
                "Tag",
                "FeatureTableTag",
                description="4-byte feature identification tag-must match FeatureTag in FeatureList",
            ),
            OtDataField(
                "Offset",
                "MinCoord",
                description="Offset to BaseCoord table-defines minimum extent value-from beginning of MinMax table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "MaxCoord",
                description="Offset to BaseCoord table-defines maximum extent value-from beginning of MinMax table-may be NULL",
            ),
        ],
    ),
    (
        "BaseCoordFormat1",
        [
            OtDataField(
                "uint16", "BaseCoordFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "int16", "Coordinate", description="X or Y value, in design units"
            ),
        ],
    ),
    (
        "BaseCoordFormat2",
        [
            OtDataField(
                "uint16", "BaseCoordFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "int16", "Coordinate", description="X or Y value, in design units"
            ),
            OtDataField(
                "GlyphID", "ReferenceGlyph", description="GlyphID of control glyph"
            ),
            OtDataField(
                "uint16",
                "BaseCoordPoint",
                description="Index of contour point on the ReferenceGlyph",
            ),
        ],
    ),
    (
        "BaseCoordFormat3",
        [
            OtDataField(
                "uint16", "BaseCoordFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "int16", "Coordinate", description="X or Y value, in design units"
            ),
            OtDataField(
                "Offset",
                "DeviceTable",
                description="Offset to Device table for X or Y value",
            ),
        ],
    ),
    #
    # jstf
    #
    (
        "JSTF",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the JSTF table-initially set to 0x00010000",
            ),
            OtDataField(
                "uint16",
                "JstfScriptCount",
                description="Number of JstfScriptRecords in this table",
            ),
            OtDataField(
                "struct",
                "JstfScriptRecord",
                repeat="JstfScriptCount",
                aux=0,
                description="Array of JstfScriptRecords-in alphabetical order, by JstfScriptTag",
            ),
        ],
    ),
    (
        "JstfScriptRecord",
        [
            OtDataField(
                "Tag", "JstfScriptTag", description="4-byte JstfScript identification"
            ),
            OtDataField(
                "Offset",
                "JstfScript",
                description="Offset to JstfScript table-from beginning of JSTF Header",
            ),
        ],
    ),
    (
        "JstfScript",
        [
            OtDataField(
                "Offset",
                "ExtenderGlyph",
                description="Offset to ExtenderGlyph table-from beginning of JstfScript table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "DefJstfLangSys",
                description="Offset to Default JstfLangSys table-from beginning of JstfScript table-may be NULL",
            ),
            OtDataField(
                "uint16",
                "JstfLangSysCount",
                description="Number of JstfLangSysRecords in this table- may be zero (0)",
            ),
            OtDataField(
                "struct",
                "JstfLangSysRecord",
                repeat="JstfLangSysCount",
                aux=0,
                description="Array of JstfLangSysRecords-in alphabetical order, by JstfLangSysTag",
            ),
        ],
    ),
    (
        "JstfLangSysRecord",
        [
            OtDataField(
                "Tag", "JstfLangSysTag", description="4-byte JstfLangSys identifier"
            ),
            OtDataField(
                "Offset",
                "JstfLangSys",
                description="Offset to JstfLangSys table-from beginning of JstfScript table",
            ),
        ],
    ),
    (
        "ExtenderGlyph",
        [
            OtDataField(
                "uint16",
                "GlyphCount",
                description="Number of Extender Glyphs in this script",
            ),
            OtDataField(
                "GlyphID",
                "ExtenderGlyph",
                repeat="GlyphCount",
                aux=0,
                description="GlyphIDs-in increasing numerical order",
            ),
        ],
    ),
    (
        "JstfLangSys",
        [
            OtDataField(
                "uint16",
                "JstfPriorityCount",
                description="Number of JstfPriority tables",
            ),
            OtDataField(
                "Offset",
                "JstfPriority",
                repeat="JstfPriorityCount",
                aux=0,
                description="Array of offsets to JstfPriority tables-from beginning of JstfLangSys table-in priority order",
            ),
        ],
    ),
    (
        "JstfPriority",
        [
            OtDataField(
                "Offset",
                "ShrinkageEnableGSUB",
                description="Offset to Shrinkage Enable JstfGSUBModList table-from beginning of JstfPriority table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ShrinkageDisableGSUB",
                description="Offset to Shrinkage Disable JstfGSUBModList table-from beginning of JstfPriority table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ShrinkageEnableGPOS",
                description="Offset to Shrinkage Enable JstfGPOSModList table-from beginning of JstfPriority table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ShrinkageDisableGPOS",
                description="Offset to Shrinkage Disable JstfGPOSModList table-from beginning of JstfPriority table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ShrinkageJstfMax",
                description="Offset to Shrinkage JstfMax table-from beginning of JstfPriority table -may be NULL",
            ),
            OtDataField(
                "Offset",
                "ExtensionEnableGSUB",
                description="Offset to Extension Enable JstfGSUBModList table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ExtensionDisableGSUB",
                description="Offset to Extension Disable JstfGSUBModList table-from beginning of JstfPriority table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ExtensionEnableGPOS",
                description="Offset to Extension Enable JstfGSUBModList table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ExtensionDisableGPOS",
                description="Offset to Extension Disable JstfGSUBModList table-from beginning of JstfPriority table-may be NULL",
            ),
            OtDataField(
                "Offset",
                "ExtensionJstfMax",
                description="Offset to Extension JstfMax table-from beginning of JstfPriority table -may be NULL",
            ),
        ],
    ),
    (
        "JstfGSUBModList",
        [
            OtDataField(
                "uint16",
                "LookupCount",
                description="Number of lookups for this modification",
            ),
            OtDataField(
                "uint16",
                "GSUBLookupIndex",
                repeat="LookupCount",
                aux=0,
                description="Array of LookupIndex identifiers in GSUB-in increasing numerical order",
            ),
        ],
    ),
    (
        "JstfGPOSModList",
        [
            OtDataField(
                "uint16",
                "LookupCount",
                description="Number of lookups for this modification",
            ),
            OtDataField(
                "uint16",
                "GPOSLookupIndex",
                repeat="LookupCount",
                aux=0,
                description="Array of LookupIndex identifiers in GPOS-in increasing numerical order",
            ),
        ],
    ),
    (
        "JstfMax",
        [
            OtDataField(
                "uint16",
                "LookupCount",
                description="Number of lookup Indices for this modification",
            ),
            OtDataField(
                "Offset",
                "Lookup",
                repeat="LookupCount",
                aux=0,
                description="Array of offsets to GPOS-type lookup tables-from beginning of JstfMax table-in design order",
            ),
        ],
    ),
    #
    # STAT
    #
    (
        "STAT",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the table-initially set to 0x00010000, currently 0x00010002.",
            ),
            OtDataField(
                "uint16",
                "DesignAxisRecordSize",
                description="Size in bytes of each design axis record",
            ),
            OtDataField(
                "uint16", "DesignAxisCount", description="Number of design axis records"
            ),
            OtDataField(
                "LOffsetTo(AxisRecordArray)",
                "DesignAxisRecord",
                description="Offset in bytes from the beginning of the STAT table to the start of the design axes array",
            ),
            OtDataField(
                "uint16", "AxisValueCount", description="Number of axis value tables"
            ),
            OtDataField(
                "LOffsetTo(AxisValueArray)",
                "AxisValueArray",
                description="Offset in bytes from the beginning of the STAT table to the start of the axes value offset array",
            ),
            OtDataField(
                "NameID",
                "ElidedFallbackNameID",
                aux="Version >= 0x00010001",
                description="NameID to use when all style attributes are elided.",
            ),
        ],
    ),
    (
        "AxisRecordArray",
        [
            OtDataField(
                "AxisRecord",
                "Axis",
                repeat="DesignAxisCount",
                aux=0,
                description="Axis records",
            ),
        ],
    ),
    (
        "AxisRecord",
        [
            OtDataField(
                "Tag",
                "AxisTag",
                description="A tag identifying the axis of design variation",
            ),
            OtDataField(
                "NameID",
                "AxisNameID",
                description='The name ID for entries in the "name" table that provide a display string for this axis',
            ),
            OtDataField(
                "uint16",
                "AxisOrdering",
                description="A value that applications can use to determine primary sorting of face names, or for ordering of descriptors when composing family or face names",
            ),
            OtDataField(
                "uint8",
                "MoreBytes",
                repeat="DesignAxisRecordSize",
                aux=-8,
                description="Extra bytes.  Set to empty array.",
            ),
        ],
    ),
    (
        "AxisValueArray",
        [
            OtDataField(
                "Offset",
                "AxisValue",
                repeat="AxisValueCount",
                aux=0,
                description="Axis values",
            ),
        ],
    ),
    (
        "AxisValueFormat1",
        [
            OtDataField("uint16", "Format", description="Format, = 1"),
            OtDataField(
                "uint16",
                "AxisIndex",
                description="Index into the axis record array identifying the axis of design variation to which the axis value record applies.",
            ),
            OtDataField("STATFlags", "Flags", description="Flags."),
            OtDataField("NameID", "ValueNameID"),
            OtDataField("Fixed", "Value"),
        ],
    ),
    (
        "AxisValueFormat2",
        [
            OtDataField("uint16", "Format", description="Format, = 2"),
            OtDataField(
                "uint16",
                "AxisIndex",
                description="Index into the axis record array identifying the axis of design variation to which the axis value record applies.",
            ),
            OtDataField("STATFlags", "Flags", description="Flags."),
            OtDataField("NameID", "ValueNameID"),
            OtDataField("Fixed", "NominalValue"),
            OtDataField("Fixed", "RangeMinValue"),
            OtDataField("Fixed", "RangeMaxValue"),
        ],
    ),
    (
        "AxisValueFormat3",
        [
            OtDataField("uint16", "Format", description="Format, = 3"),
            OtDataField(
                "uint16",
                "AxisIndex",
                description="Index into the axis record array identifying the axis of design variation to which the axis value record applies.",
            ),
            OtDataField("STATFlags", "Flags", description="Flags."),
            OtDataField("NameID", "ValueNameID"),
            OtDataField("Fixed", "Value"),
            OtDataField("Fixed", "LinkedValue"),
        ],
    ),
    (
        "AxisValueFormat4",
        [
            OtDataField("uint16", "Format", description="Format, = 4"),
            OtDataField(
                "uint16",
                "AxisCount",
                description="The total number of axes contributing to this axis-values combination.",
            ),
            OtDataField("STATFlags", "Flags", description="Flags."),
            OtDataField("NameID", "ValueNameID"),
            OtDataField(
                "struct",
                "AxisValueRecord",
                repeat="AxisCount",
                aux=0,
                description="Array of AxisValue records that provide the combination of axis values, one for each contributing axis. ",
            ),
        ],
    ),
    (
        "AxisValueRecord",
        [
            OtDataField(
                "uint16",
                "AxisIndex",
                description="Index into the axis record array identifying the axis of design variation to which the axis value record applies.",
            ),
            OtDataField(
                "Fixed",
                "Value",
                description="A numeric value for this attribute value.",
            ),
        ],
    ),
    #
    # Variation fonts
    #
    # GSUB/GPOS FeatureVariations
    (
        "FeatureVariations",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the table-initially set to 0x00010000",
            ),
            OtDataField(
                "uint32",
                "FeatureVariationCount",
                description="Number of records in the FeatureVariationRecord array",
            ),
            OtDataField(
                "struct",
                "FeatureVariationRecord",
                repeat="FeatureVariationCount",
                aux=0,
                description="Array of FeatureVariationRecord",
            ),
        ],
    ),
    (
        "FeatureVariationRecord",
        [
            OtDataField(
                "LOffset",
                "ConditionSet",
                description="Offset to a ConditionSet table, from beginning of the FeatureVariations table.",
            ),
            OtDataField(
                "LOffset",
                "FeatureTableSubstitution",
                description="Offset to a FeatureTableSubstitution table, from beginning of the FeatureVariations table",
            ),
        ],
    ),
    (
        "ConditionList",
        [
            OtDataField(
                "uint32",
                "ConditionCount",
                description="Number of condition tables in the ConditionTable array",
            ),
            OtDataField(
                "LOffset",
                "ConditionTable",
                repeat="ConditionCount",
                aux=0,
                description="Array of offset to condition tables, from the beginning of the ConditionList table.",
            ),
        ],
    ),
    (
        "ConditionSet",
        [
            OtDataField(
                "uint16",
                "ConditionCount",
                description="Number of condition tables in the ConditionTable array",
            ),
            OtDataField(
                "LOffset",
                "ConditionTable",
                repeat="ConditionCount",
                aux=0,
                description="Array of offset to condition tables, from the beginning of the ConditionSet table.",
            ),
        ],
    ),
    (
        "ConditionTableFormat1",
        [
            OtDataField("uint16", "Format", description="Format, = 1"),
            OtDataField(
                "uint16",
                "AxisIndex",
                description="Index for the variation axis within the fvar table, base 0.",
            ),
            OtDataField(
                "F2Dot14",
                "FilterRangeMinValue",
                description="Minimum normalized axis value of the font variation instances that satisfy this condition.",
            ),
            OtDataField(
                "F2Dot14",
                "FilterRangeMaxValue",
                description="Maximum value that satisfies this condition.",
            ),
        ],
    ),
    (
        "ConditionTableFormat2",
        [
            OtDataField("uint16", "Format", description="Format, = 2"),
            OtDataField(
                "int16", "DefaultValue", description="Value at default instance."
            ),
            OtDataField(
                "uint32",
                "VarIdx",
                description="Variation index to vary the value based on current designspace location.",
            ),
        ],
    ),
    (
        "ConditionTableFormat3",
        [
            OtDataField("uint16", "Format", description="Format, = 3"),
            OtDataField(
                "uint8",
                "ConditionCount",
                description="Index for the variation axis within the fvar table, base 0.",
            ),
            OtDataField(
                "Offset24",
                "ConditionTable",
                repeat="ConditionCount",
                aux=0,
                description="Array of condition tables for this conjunction (AND) expression.",
            ),
        ],
    ),
    (
        "ConditionTableFormat4",
        [
            OtDataField("uint16", "Format", description="Format, = 4"),
            OtDataField(
                "uint8",
                "ConditionCount",
                description="Index for the variation axis within the fvar table, base 0.",
            ),
            OtDataField(
                "Offset24",
                "ConditionTable",
                repeat="ConditionCount",
                aux=0,
                description="Array of condition tables for this disjunction (OR) expression.",
            ),
        ],
    ),
    (
        "ConditionTableFormat5",
        [
            OtDataField("uint16", "Format", description="Format, = 5"),
            OtDataField(
                "Offset24", "ConditionTable", description="Condition to negate."
            ),
        ],
    ),
    (
        "FeatureTableSubstitution",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the table-initially set to 0x00010000",
            ),
            OtDataField(
                "uint16",
                "SubstitutionCount",
                description="Number of records in the FeatureVariationRecords array",
            ),
            OtDataField(
                "FeatureTableSubstitutionRecord",
                "SubstitutionRecord",
                repeat="SubstitutionCount",
                aux=0,
                description="Array of FeatureTableSubstitutionRecord",
            ),
        ],
    ),
    (
        "FeatureTableSubstitutionRecord",
        [
            OtDataField(
                "uint16",
                "FeatureIndex",
                description="The feature table index to match.",
            ),
            OtDataField(
                "LOffset",
                "Feature",
                description="Offset to an alternate feature table, from start of the FeatureTableSubstitution table.",
            ),
        ],
    ),
    # VariationStore
    (
        "VarRegionAxis",
        [
            OtDataField("F2Dot14", "StartCoord"),
            OtDataField("F2Dot14", "PeakCoord"),
            OtDataField("F2Dot14", "EndCoord"),
        ],
    ),
    (
        "VarRegion",
        [
            OtDataField("struct", "VarRegionAxis", repeat="RegionAxisCount", aux=0),
        ],
    ),
    (
        "VarRegionList",
        [
            OtDataField("uint16", "RegionAxisCount"),
            OtDataField("uint16", "RegionCount"),
            OtDataField("VarRegion", "Region", repeat="RegionCount", aux=0),
        ],
    ),
    (
        "VarData",
        [
            OtDataField("uint16", "ItemCount"),
            OtDataField("uint16", "NumShorts"),
            OtDataField("uint16", "VarRegionCount"),
            OtDataField("uint16", "VarRegionIndex", repeat="VarRegionCount", aux=0),
            OtDataField("VarDataValue", "Item", repeat="ItemCount", aux=0),
        ],
    ),
    (
        "VarStore",
        [
            OtDataField("uint16", "Format", description="Set to 1."),
            OtDataField("LOffset", "VarRegionList"),
            OtDataField("uint16", "VarDataCount"),
            OtDataField("LOffset", "VarData", repeat="VarDataCount", aux=0),
        ],
    ),
    # Variation helpers
    (
        "VarIdxMap",
        [
            OtDataField("uint16", "EntryFormat"),  # Automatically computed
            OtDataField("uint16", "MappingCount"),  # Automatically computed
            OtDataField(
                "VarIdxMapValue",
                "mapping",
                aux=0,
                description="Array of compressed data",
            ),
        ],
    ),
    (
        "DeltaSetIndexMapFormat0",
        [
            OtDataField(
                "uint8", "Format", description="Format of the DeltaSetIndexMap = 0"
            ),
            OtDataField("uint8", "EntryFormat"),  # Automatically computed
            OtDataField("uint16", "MappingCount"),  # Automatically computed
            OtDataField(
                "VarIdxMapValue",
                "mapping",
                aux=0,
                description="Array of compressed data",
            ),
        ],
    ),
    (
        "DeltaSetIndexMapFormat1",
        [
            OtDataField(
                "uint8", "Format", description="Format of the DeltaSetIndexMap = 1"
            ),
            OtDataField("uint8", "EntryFormat"),  # Automatically computed
            OtDataField("uint32", "MappingCount"),  # Automatically computed
            OtDataField(
                "VarIdxMapValue",
                "mapping",
                aux=0,
                description="Array of compressed data",
            ),
        ],
    ),
    # MultiVariationStore
    (
        "SparseVarRegionAxis",
        [
            OtDataField("uint16", "AxisIndex"),
            OtDataField("F2Dot14", "StartCoord"),
            OtDataField("F2Dot14", "PeakCoord"),
            OtDataField("F2Dot14", "EndCoord"),
        ],
    ),
    (
        "SparseVarRegion",
        [
            OtDataField("uint16", "SparseRegionCount"),
            OtDataField(
                "struct", "SparseVarRegionAxis", repeat="SparseRegionCount", aux=0
            ),
        ],
    ),
    (
        "SparseVarRegionList",
        [
            OtDataField("uint16", "RegionCount"),
            OtDataField(
                "LOffsetTo(SparseVarRegion)", "Region", repeat="RegionCount", aux=0
            ),
        ],
    ),
    (
        "MultiVarData",
        [
            OtDataField("uint8", "Format", description="Set to 1."),
            OtDataField("uint16", "VarRegionCount"),
            OtDataField("uint16", "VarRegionIndex", repeat="VarRegionCount", aux=0),
            OtDataField("TupleList", "Item", aux=0),
        ],
    ),
    (
        "MultiVarStore",
        [
            OtDataField("uint16", "Format", description="Set to 1."),
            OtDataField("LOffset", "SparseVarRegionList"),
            OtDataField("uint16", "MultiVarDataCount"),
            OtDataField("LOffset", "MultiVarData", repeat="MultiVarDataCount", aux=0),
        ],
    ),
    # VariableComposites
    (
        "VARC",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the HVAR table-initially = 0x00010000",
            ),
            OtDataField("LOffset", "Coverage"),
            OtDataField("LOffset", "MultiVarStore", description="(may be NULL)"),
            OtDataField("LOffset", "ConditionList", description="(may be NULL)"),
            OtDataField("LOffset", "AxisIndicesList", description="(may be NULL)"),
            OtDataField("LOffset", "VarCompositeGlyphs"),
        ],
    ),
    (
        "AxisIndicesList",
        [
            OtDataField("TupleList", "Item", aux=0),
        ],
    ),
    (
        "VarCompositeGlyphs",
        [
            OtDataField("VarCompositeGlyphList", "VarCompositeGlyph"),
        ],
    ),
    # Glyph advance variations
    (
        "HVAR",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the HVAR table-initially = 0x00010000",
            ),
            OtDataField("LOffset", "VarStore"),
            OtDataField("LOffsetTo(VarIdxMap)", "AdvWidthMap"),
            OtDataField("LOffsetTo(VarIdxMap)", "LsbMap"),
            OtDataField("LOffsetTo(VarIdxMap)", "RsbMap"),
        ],
    ),
    (
        "VVAR",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the VVAR table-initially = 0x00010000",
            ),
            OtDataField("LOffset", "VarStore"),
            OtDataField("LOffsetTo(VarIdxMap)", "AdvHeightMap"),
            OtDataField("LOffsetTo(VarIdxMap)", "TsbMap"),
            OtDataField("LOffsetTo(VarIdxMap)", "BsbMap"),
            OtDataField(
                "LOffsetTo(VarIdxMap)",
                "VOrgMap",
                description="Vertical origin mapping.",
            ),
        ],
    ),
    # Font-wide metrics variations
    (
        "MetricsValueRecord",
        [
            OtDataField(
                "Tag", "ValueTag", description="4-byte font-wide measure identifier"
            ),
            OtDataField(
                "uint32", "VarIdx", description="Combined outer-inner variation index"
            ),
            OtDataField(
                "uint8",
                "MoreBytes",
                repeat="ValueRecordSize",
                aux=-8,
                description="Extra bytes.  Set to empty array.",
            ),
        ],
    ),
    (
        "MVAR",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the MVAR table-initially = 0x00010000",
            ),
            OtDataField("uint16", "Reserved", description="Set to 0"),
            OtDataField("uint16", "ValueRecordSize"),
            OtDataField("uint16", "ValueRecordCount"),
            OtDataField("Offset", "VarStore"),
            OtDataField(
                "MetricsValueRecord", "ValueRecord", repeat="ValueRecordCount", aux=0
            ),
        ],
    ),
    #
    # math
    #
    (
        "MATH",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the MATH table-initially set to 0x00010000.",
            ),
            OtDataField(
                "Offset",
                "MathConstants",
                description="Offset to MathConstants table - from the beginning of MATH table.",
            ),
            OtDataField(
                "Offset",
                "MathGlyphInfo",
                description="Offset to MathGlyphInfo table - from the beginning of MATH table.",
            ),
            OtDataField(
                "Offset",
                "MathVariants",
                description="Offset to MathVariants table - from the beginning of MATH table.",
            ),
        ],
    ),
    (
        "MathValueRecord",
        [
            OtDataField(
                "int16", "Value", description="The X or Y value in design units."
            ),
            OtDataField(
                "Offset",
                "DeviceTable",
                description="Offset to the device table - from the beginning of parent table. May be NULL. Suggested format for device table is 1.",
            ),
        ],
    ),
    (
        "MathConstants",
        [
            OtDataField(
                "int16",
                "ScriptPercentScaleDown",
                description="Percentage of scaling down for script level 1. Suggested value: 80%.",
            ),
            OtDataField(
                "int16",
                "ScriptScriptPercentScaleDown",
                description="Percentage of scaling down for script level 2 (ScriptScript). Suggested value: 60%.",
            ),
            OtDataField(
                "uint16",
                "DelimitedSubFormulaMinHeight",
                description="Minimum height required for a delimited expression to be treated as a subformula. Suggested value: normal line height x1.5.",
            ),
            OtDataField(
                "uint16",
                "DisplayOperatorMinHeight",
                description="Minimum height of n-ary operators (such as integral and summation) for formulas in display mode.",
            ),
            OtDataField(
                "MathValueRecord",
                "MathLeading",
                description="White space to be left between math formulas to ensure proper line spacing. For example, for applications that treat line gap as a part of line ascender, formulas with ink  going above (os2.sTypoAscender + os2.sTypoLineGap - MathLeading) or with ink going below os2.sTypoDescender will result in increasing line height.",
            ),
            OtDataField(
                "MathValueRecord", "AxisHeight", description="Axis height of the font."
            ),
            OtDataField(
                "MathValueRecord",
                "AccentBaseHeight",
                description="Maximum (ink) height of accent base that does not require raising the accents. Suggested: x-height of the font (os2.sxHeight) plus any possible overshots.",
            ),
            OtDataField(
                "MathValueRecord",
                "FlattenedAccentBaseHeight",
                description="Maximum (ink) height of accent base that does not require flattening the accents. Suggested: cap height of the font (os2.sCapHeight).",
            ),
            OtDataField(
                "MathValueRecord",
                "SubscriptShiftDown",
                description="The standard shift down applied to subscript elements. Positive for moving in the downward direction. Suggested: os2.ySubscriptYOffset.",
            ),
            OtDataField(
                "MathValueRecord",
                "SubscriptTopMax",
                description="Maximum allowed height of the (ink) top of subscripts that does not require moving subscripts further down. Suggested: 4/5 x-height.",
            ),
            OtDataField(
                "MathValueRecord",
                "SubscriptBaselineDropMin",
                description="Minimum allowed drop of the baseline of subscripts relative to the (ink) bottom of the base. Checked for bases that are treated as a box or extended shape. Positive for subscript baseline dropped below the base bottom.",
            ),
            OtDataField(
                "MathValueRecord",
                "SuperscriptShiftUp",
                description="Standard shift up applied to superscript elements. Suggested: os2.ySuperscriptYOffset.",
            ),
            OtDataField(
                "MathValueRecord",
                "SuperscriptShiftUpCramped",
                description="Standard shift of superscripts relative to the base, in cramped style.",
            ),
            OtDataField(
                "MathValueRecord",
                "SuperscriptBottomMin",
                description="Minimum allowed height of the (ink) bottom of superscripts that does not require moving subscripts further up. Suggested: 1/4 x-height.",
            ),
            OtDataField(
                "MathValueRecord",
                "SuperscriptBaselineDropMax",
                description="Maximum allowed drop of the baseline of superscripts relative to the (ink) top of the base. Checked for bases that are treated as a box or extended shape. Positive for superscript baseline below the base top.",
            ),
            OtDataField(
                "MathValueRecord",
                "SubSuperscriptGapMin",
                description="Minimum gap between the superscript and subscript ink. Suggested: 4x default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "SuperscriptBottomMaxWithSubscript",
                description="The maximum level to which the (ink) bottom of superscript can be pushed to increase the gap between superscript and subscript, before subscript starts being moved down. Suggested: 4/5 x-height.",
            ),
            OtDataField(
                "MathValueRecord",
                "SpaceAfterScript",
                description="Extra white space to be added after each subscript and superscript. Suggested: 0.5pt for a 12 pt font.",
            ),
            OtDataField(
                "MathValueRecord",
                "UpperLimitGapMin",
                description="Minimum gap between the (ink) bottom of the upper limit, and the (ink) top of the base operator.",
            ),
            OtDataField(
                "MathValueRecord",
                "UpperLimitBaselineRiseMin",
                description="Minimum distance between baseline of upper limit and (ink) top of the base operator.",
            ),
            OtDataField(
                "MathValueRecord",
                "LowerLimitGapMin",
                description="Minimum gap between (ink) top of the lower limit, and (ink) bottom of the base operator.",
            ),
            OtDataField(
                "MathValueRecord",
                "LowerLimitBaselineDropMin",
                description="Minimum distance between baseline of the lower limit and (ink) bottom of the base operator.",
            ),
            OtDataField(
                "MathValueRecord",
                "StackTopShiftUp",
                description="Standard shift up applied to the top element of a stack.",
            ),
            OtDataField(
                "MathValueRecord",
                "StackTopDisplayStyleShiftUp",
                description="Standard shift up applied to the top element of a stack in display style.",
            ),
            OtDataField(
                "MathValueRecord",
                "StackBottomShiftDown",
                description="Standard shift down applied to the bottom element of a stack. Positive for moving in the downward direction.",
            ),
            OtDataField(
                "MathValueRecord",
                "StackBottomDisplayStyleShiftDown",
                description="Standard shift down applied to the bottom element of a stack in display style. Positive for moving in the downward direction.",
            ),
            OtDataField(
                "MathValueRecord",
                "StackGapMin",
                description="Minimum gap between (ink) bottom of the top element of a stack, and the (ink) top of the bottom element. Suggested: 3x default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "StackDisplayStyleGapMin",
                description="Minimum gap between (ink) bottom of the top element of a stack, and the (ink) top of the bottom element in display style. Suggested: 7x default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "StretchStackTopShiftUp",
                description="Standard shift up applied to the top element of the stretch stack.",
            ),
            OtDataField(
                "MathValueRecord",
                "StretchStackBottomShiftDown",
                description="Standard shift down applied to the bottom element of the stretch stack. Positive for moving in the downward direction.",
            ),
            OtDataField(
                "MathValueRecord",
                "StretchStackGapAboveMin",
                description="Minimum gap between the ink of the stretched element, and the (ink) bottom of the element above. Suggested: UpperLimitGapMin",
            ),
            OtDataField(
                "MathValueRecord",
                "StretchStackGapBelowMin",
                description="Minimum gap between the ink of the stretched element, and the (ink) top of the element below. Suggested: LowerLimitGapMin.",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionNumeratorShiftUp",
                description="Standard shift up applied to the numerator.",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionNumeratorDisplayStyleShiftUp",
                description="Standard shift up applied to the numerator in display style. Suggested: StackTopDisplayStyleShiftUp.",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionDenominatorShiftDown",
                description="Standard shift down applied to the denominator. Positive for moving in the downward direction.",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionDenominatorDisplayStyleShiftDown",
                description="Standard shift down applied to the denominator in display style. Positive for moving in the downward direction. Suggested: StackBottomDisplayStyleShiftDown.",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionNumeratorGapMin",
                description="Minimum tolerated gap between the (ink) bottom of the numerator and the ink of the fraction bar. Suggested: default rule thickness",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionNumDisplayStyleGapMin",
                description="Minimum tolerated gap between the (ink) bottom of the numerator and the ink of the fraction bar in display style. Suggested: 3x default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionRuleThickness",
                description="Thickness of the fraction bar. Suggested: default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionDenominatorGapMin",
                description="Minimum tolerated gap between the (ink) top of the denominator and the ink of the fraction bar. Suggested: default rule thickness",
            ),
            OtDataField(
                "MathValueRecord",
                "FractionDenomDisplayStyleGapMin",
                description="Minimum tolerated gap between the (ink) top of the denominator and the ink of the fraction bar in display style. Suggested: 3x default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "SkewedFractionHorizontalGap",
                description="Horizontal distance between the top and bottom elements of a skewed fraction.",
            ),
            OtDataField(
                "MathValueRecord",
                "SkewedFractionVerticalGap",
                description="Vertical distance between the ink of the top and bottom elements of a skewed fraction.",
            ),
            OtDataField(
                "MathValueRecord",
                "OverbarVerticalGap",
                description="Distance between the overbar and the (ink) top of he base. Suggested: 3x default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "OverbarRuleThickness",
                description="Thickness of overbar. Suggested: default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "OverbarExtraAscender",
                description="Extra white space reserved above the overbar. Suggested: default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "UnderbarVerticalGap",
                description="Distance between underbar and (ink) bottom of the base. Suggested: 3x default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "UnderbarRuleThickness",
                description="Thickness of underbar. Suggested: default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "UnderbarExtraDescender",
                description="Extra white space reserved below the underbar. Always positive. Suggested: default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "RadicalVerticalGap",
                description="Space between the (ink) top of the expression and the bar over it. Suggested: 1 1/4 default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "RadicalDisplayStyleVerticalGap",
                description="Space between the (ink) top of the expression and the bar over it. Suggested: default rule thickness + 1/4 x-height.",
            ),
            OtDataField(
                "MathValueRecord",
                "RadicalRuleThickness",
                description="Thickness of the radical rule. This is the thickness of the rule in designed or constructed radical signs. Suggested: default rule thickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "RadicalExtraAscender",
                description="Extra white space reserved above the radical. Suggested: RadicalRuleThickness.",
            ),
            OtDataField(
                "MathValueRecord",
                "RadicalKernBeforeDegree",
                description="Extra horizontal kern before the degree of a radical, if such is present. Suggested: 5/18 of em.",
            ),
            OtDataField(
                "MathValueRecord",
                "RadicalKernAfterDegree",
                description="Negative kern after the degree of a radical, if such is present. Suggested: 10/18 of em.",
            ),
            OtDataField(
                "uint16",
                "RadicalDegreeBottomRaisePercent",
                description="Height of the bottom of the radical degree, if such is present, in proportion to the ascender of the radical sign. Suggested: 60%.",
            ),
        ],
    ),
    (
        "MathGlyphInfo",
        [
            OtDataField(
                "Offset",
                "MathItalicsCorrectionInfo",
                description="Offset to MathItalicsCorrectionInfo table - from the beginning of MathGlyphInfo table.",
            ),
            OtDataField(
                "Offset",
                "MathTopAccentAttachment",
                description="Offset to MathTopAccentAttachment table - from the beginning of MathGlyphInfo table.",
            ),
            OtDataField(
                "Offset",
                "ExtendedShapeCoverage",
                description="Offset to coverage table for Extended Shape glyphs - from the  beginning of MathGlyphInfo table. When the left or right glyph of a box is an extended shape variant, the (ink) box (and not the default position defined by values in MathConstants table) should be used for vertical positioning purposes. May be NULL.",
            ),
            OtDataField(
                "Offset",
                "MathKernInfo",
                description="Offset to MathKernInfo table - from the beginning of MathGlyphInfo table.",
            ),
        ],
    ),
    (
        "MathItalicsCorrectionInfo",
        [
            OtDataField(
                "Offset",
                "Coverage",
                description="Offset to Coverage table - from the beginning of MathItalicsCorrectionInfo table.",
            ),
            OtDataField(
                "uint16",
                "ItalicsCorrectionCount",
                description="Number of italics correction values. Should coincide with the number of covered glyphs.",
            ),
            OtDataField(
                "MathValueRecord",
                "ItalicsCorrection",
                repeat="ItalicsCorrectionCount",
                aux=0,
                description="Array of MathValueRecords defining italics correction values for each covered glyph.",
            ),
        ],
    ),
    (
        "MathTopAccentAttachment",
        [
            OtDataField(
                "Offset",
                "TopAccentCoverage",
                description="Offset to Coverage table - from the beginning of  MathTopAccentAttachment table.",
            ),
            OtDataField(
                "uint16",
                "TopAccentAttachmentCount",
                description="Number of top accent attachment point values. Should coincide with the number of covered glyphs",
            ),
            OtDataField(
                "MathValueRecord",
                "TopAccentAttachment",
                repeat="TopAccentAttachmentCount",
                aux=0,
                description="Array of MathValueRecords defining top accent attachment points for each covered glyph",
            ),
        ],
    ),
    (
        "MathKernInfo",
        [
            OtDataField(
                "Offset",
                "MathKernCoverage",
                description="Offset to Coverage table - from the beginning of the MathKernInfo table.",
            ),
            OtDataField(
                "uint16", "MathKernCount", description="Number of MathKernInfoRecords."
            ),
            OtDataField(
                "MathKernInfoRecord",
                "MathKernInfoRecords",
                repeat="MathKernCount",
                aux=0,
                description="Array of MathKernInfoRecords, per-glyph information for mathematical positioning of subscripts and superscripts.",
            ),
        ],
    ),
    (
        "MathKernInfoRecord",
        [
            OtDataField(
                "Offset",
                "TopRightMathKern",
                description="Offset to MathKern table for top right corner - from the beginning of MathKernInfo table. May be NULL.",
            ),
            OtDataField(
                "Offset",
                "TopLeftMathKern",
                description="Offset to MathKern table for the top left corner - from the beginning of MathKernInfo table. May be NULL.",
            ),
            OtDataField(
                "Offset",
                "BottomRightMathKern",
                description="Offset to MathKern table for bottom right corner - from the beginning of MathKernInfo table. May be NULL.",
            ),
            OtDataField(
                "Offset",
                "BottomLeftMathKern",
                description="Offset to MathKern table for bottom left corner - from the beginning of MathKernInfo table. May be NULL.",
            ),
        ],
    ),
    (
        "MathKern",
        [
            OtDataField(
                "uint16",
                "HeightCount",
                description="Number of heights on which the kern value changes.",
            ),
            OtDataField(
                "MathValueRecord",
                "CorrectionHeight",
                repeat="HeightCount",
                aux=0,
                description="Array of correction heights at which the kern value changes. Sorted by the height value in design units.",
            ),
            OtDataField(
                "MathValueRecord",
                "KernValue",
                repeat="HeightCount",
                aux=1,
                description="Array of kern values corresponding to heights. First value is the kern value for all heights less or equal than the first height in this table.Last value is the value to be applied for all heights greater than the last height in this table. Negative values are interpreted as move glyphs closer to each other.",
            ),
        ],
    ),
    (
        "MathVariants",
        [
            OtDataField(
                "uint16",
                "MinConnectorOverlap",
                description="Minimum overlap of connecting glyphs during glyph construction,  in design units.",
            ),
            OtDataField(
                "Offset",
                "VertGlyphCoverage",
                description="Offset to Coverage table - from the beginning of MathVariants table.",
            ),
            OtDataField(
                "Offset",
                "HorizGlyphCoverage",
                description="Offset to Coverage table - from the beginning of MathVariants table.",
            ),
            OtDataField(
                "uint16",
                "VertGlyphCount",
                description="Number of glyphs for which information is provided for vertically growing variants.",
            ),
            OtDataField(
                "uint16",
                "HorizGlyphCount",
                description="Number of glyphs for which information is provided for horizontally growing variants.",
            ),
            OtDataField(
                "Offset",
                "VertGlyphConstruction",
                repeat="VertGlyphCount",
                aux=0,
                description="Array of offsets to MathGlyphConstruction tables - from the beginning of the MathVariants table, for shapes growing in vertical direction.",
            ),
            OtDataField(
                "Offset",
                "HorizGlyphConstruction",
                repeat="HorizGlyphCount",
                aux=0,
                description="Array of offsets to MathGlyphConstruction tables - from the beginning of the MathVariants table, for shapes growing in horizontal direction.",
            ),
        ],
    ),
    (
        "MathGlyphConstruction",
        [
            OtDataField(
                "Offset",
                "GlyphAssembly",
                description="Offset to GlyphAssembly table for this shape - from the beginning of MathGlyphConstruction table. May be NULL",
            ),
            OtDataField(
                "uint16",
                "VariantCount",
                description="Count of glyph growing variants for this glyph.",
            ),
            OtDataField(
                "MathGlyphVariantRecord",
                "MathGlyphVariantRecord",
                repeat="VariantCount",
                aux=0,
                description="MathGlyphVariantRecords for alternative variants of the glyphs.",
            ),
        ],
    ),
    (
        "MathGlyphVariantRecord",
        [
            OtDataField(
                "GlyphID", "VariantGlyph", description="Glyph ID for the variant."
            ),
            OtDataField(
                "uint16",
                "AdvanceMeasurement",
                description="Advance width/height, in design units, of the variant, in the direction of requested glyph extension.",
            ),
        ],
    ),
    (
        "GlyphAssembly",
        [
            OtDataField(
                "MathValueRecord",
                "ItalicsCorrection",
                description="Italics correction of this GlyphAssembly. Should not depend on the assembly size.",
            ),
            OtDataField(
                "uint16", "PartCount", description="Number of parts in this assembly."
            ),
            OtDataField(
                "GlyphPartRecord",
                "PartRecords",
                repeat="PartCount",
                aux=0,
                description="Array of part records, from left to right and bottom to top.",
            ),
        ],
    ),
    (
        "GlyphPartRecord",
        [
            OtDataField("GlyphID", "glyph", description="Glyph ID for the part."),
            OtDataField(
                "uint16",
                "StartConnectorLength",
                description="Advance width/ height of the straight bar connector material, in design units, is at the beginning of the glyph, in the direction of the extension.",
            ),
            OtDataField(
                "uint16",
                "EndConnectorLength",
                description="Advance width/ height of the straight bar connector material, in design units, is at the end of the glyph, in the direction of the extension.",
            ),
            OtDataField(
                "uint16",
                "FullAdvance",
                description="Full advance width/height for this part, in the direction of the extension. In design units.",
            ),
            OtDataField(
                "uint16",
                "PartFlags",
                description="Part qualifiers. PartFlags enumeration currently uses only one bit: 0x0001 fExtender: If set, the part can be skipped or repeated. 0xFFFE Reserved",
            ),
        ],
    ),
    ##
    ## Apple Advanced Typography (AAT) tables
    ##
    (
        "AATLookupSegment",
        [
            OtDataField(
                "uint16", "lastGlyph", description="Last glyph index in this segment."
            ),
            OtDataField(
                "uint16", "firstGlyph", description="First glyph index in this segment."
            ),
            OtDataField(
                "uint16",
                "value",
                description="A 16-bit offset from the start of the table to the data.",
            ),
        ],
    ),
    #
    # ankr
    #
    (
        "ankr",
        [
            OtDataField("struct", "AnchorPoints", description="Anchor points table."),
        ],
    ),
    (
        "AnchorPointsFormat0",
        [
            OtDataField(
                "uint16",
                "Format",
                description="Format of the anchor points table, = 0.",
            ),
            OtDataField(
                "uint16", "Flags", description="Flags. Currenty unused, set to zero."
            ),
            OtDataField(
                "AATLookupWithDataOffset(AnchorGlyphData)",
                "Anchors",
                description="Table of with anchor overrides for each glyph.",
            ),
        ],
    ),
    (
        "AnchorGlyphData",
        [
            OtDataField(
                "uint32",
                "AnchorPointCount",
                description="Number of anchor points for this glyph.",
            ),
            OtDataField(
                "struct",
                "AnchorPoint",
                repeat="AnchorPointCount",
                aux=0,
                description="Individual anchor points.",
            ),
        ],
    ),
    (
        "AnchorPoint",
        [
            OtDataField(
                "int16", "XCoordinate", description="X coordinate of this anchor point."
            ),
            OtDataField(
                "int16", "YCoordinate", description="Y coordinate of this anchor point."
            ),
        ],
    ),
    #
    # bsln
    #
    (
        "bsln",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version number of the AAT baseline table (0x00010000 for the initial version).",
            ),
            OtDataField("struct", "Baseline", description="Baseline table."),
        ],
    ),
    (
        "BaselineFormat0",
        [
            OtDataField(
                "uint16", "Format", description="Format of the baseline table, = 0."
            ),
            OtDataField(
                "uint16",
                "DefaultBaseline",
                description="Default baseline value for all glyphs. This value can be from 0 through 31.",
            ),
            OtDataField(
                "uint16",
                "Delta",
                repeat=32,
                aux=0,
                description="These are the FUnit distance deltas from the font’s natural baseline to the other baselines used in the font. A total of 32 deltas must be assigned.",
            ),
        ],
    ),
    (
        "BaselineFormat1",
        [
            OtDataField(
                "uint16", "Format", description="Format of the baseline table, = 1."
            ),
            OtDataField(
                "uint16",
                "DefaultBaseline",
                description="Default baseline value for all glyphs. This value can be from 0 through 31.",
            ),
            OtDataField(
                "uint16",
                "Delta",
                repeat=32,
                aux=0,
                description="These are the FUnit distance deltas from the font’s natural baseline to the other baselines used in the font. A total of 32 deltas must be assigned.",
            ),
            OtDataField(
                "AATLookup(uint16)",
                "BaselineValues",
                description="Lookup table that maps glyphs to their baseline values.",
            ),
        ],
    ),
    (
        "BaselineFormat2",
        [
            OtDataField(
                "uint16", "Format", description="Format of the baseline table, = 1."
            ),
            OtDataField(
                "uint16",
                "DefaultBaseline",
                description="Default baseline value for all glyphs. This value can be from 0 through 31.",
            ),
            OtDataField(
                "GlyphID",
                "StandardGlyph",
                description="Glyph index of the glyph in this font to be used to set the baseline values. This glyph must contain a set of control points (whose numbers are contained in the following field) that determines baseline distances.",
            ),
            OtDataField(
                "uint16",
                "ControlPoint",
                repeat=32,
                aux=0,
                description="Array of 32 control point numbers, associated with the standard glyph. A value of 0xFFFF means there is no corresponding control point in the standard glyph.",
            ),
        ],
    ),
    (
        "BaselineFormat3",
        [
            OtDataField(
                "uint16", "Format", description="Format of the baseline table, = 1."
            ),
            OtDataField(
                "uint16",
                "DefaultBaseline",
                description="Default baseline value for all glyphs. This value can be from 0 through 31.",
            ),
            OtDataField(
                "GlyphID",
                "StandardGlyph",
                description="Glyph index of the glyph in this font to be used to set the baseline values. This glyph must contain a set of control points (whose numbers are contained in the following field) that determines baseline distances.",
            ),
            OtDataField(
                "uint16",
                "ControlPoint",
                repeat=32,
                aux=0,
                description="Array of 32 control point numbers, associated with the standard glyph. A value of 0xFFFF means there is no corresponding control point in the standard glyph.",
            ),
            OtDataField(
                "AATLookup(uint16)",
                "BaselineValues",
                description="Lookup table that maps glyphs to their baseline values.",
            ),
        ],
    ),
    #
    # cidg
    #
    (
        "cidg",
        [
            OtDataField(
                "struct", "CIDGlyphMapping", description="CID-to-glyph mapping table."
            ),
        ],
    ),
    (
        "CIDGlyphMappingFormat0",
        [
            OtDataField(
                "uint16",
                "Format",
                description="Format of the CID-to-glyph mapping table, = 0.",
            ),
            OtDataField(
                "uint16", "DataFormat", description="Currenty unused, set to zero."
            ),
            OtDataField(
                "uint32", "StructLength", description="Size of the table in bytes."
            ),
            OtDataField("uint16", "Registry", description="The registry ID."),
            OtDataField(
                "char64",
                "RegistryName",
                description="The registry name in ASCII; unused bytes should be set to 0.",
            ),
            OtDataField("uint16", "Order", description="The order ID."),
            OtDataField(
                "char64",
                "OrderName",
                description="The order name in ASCII; unused bytes should be set to 0.",
            ),
            OtDataField(
                "uint16", "SupplementVersion", description="The supplement version."
            ),
            OtDataField(
                "CIDGlyphMap",
                "Mapping",
                description="A mapping from CIDs to the glyphs in the font, starting with CID 0. If a CID from the identified collection has no glyph in the font, 0xFFFF is used",
            ),
        ],
    ),
    #
    # feat
    #
    (
        "feat",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the feat table-initially set to 0x00010000.",
            ),
            OtDataField(
                "FeatureNames", "FeatureNames", description="The feature names."
            ),
        ],
    ),
    (
        "FeatureNames",
        [
            OtDataField(
                "uint16",
                "FeatureNameCount",
                description="Number of entries in the feature name array.",
            ),
            OtDataField("uint16", "Reserved1", description="Reserved (set to zero)."),
            OtDataField("uint32", "Reserved2", description="Reserved (set to zero)."),
            OtDataField(
                "FeatureName",
                "FeatureName",
                repeat="FeatureNameCount",
                aux=0,
                description="The feature name array.",
            ),
        ],
    ),
    (
        "FeatureName",
        [
            OtDataField("uint16", "FeatureType", description="Feature type."),
            OtDataField(
                "uint16",
                "SettingsCount",
                description="The number of records in the setting name array.",
            ),
            OtDataField(
                "LOffset",
                "Settings",
                description="Offset to setting table for this feature.",
            ),
            OtDataField(
                "uint16",
                "FeatureFlags",
                description="Single-bit flags associated with the feature type.",
            ),
            OtDataField(
                "NameID",
                "FeatureNameID",
                description="The name table index for the feature name.",
            ),
        ],
    ),
    (
        "Settings",
        [
            OtDataField(
                "Setting",
                "Setting",
                repeat="SettingsCount",
                aux=0,
                description="The setting array.",
            ),
        ],
    ),
    (
        "Setting",
        [
            OtDataField("uint16", "SettingValue", description="The setting."),
            OtDataField(
                "NameID",
                "SettingNameID",
                description="The name table index for the setting name.",
            ),
        ],
    ),
    #
    # gcid
    #
    (
        "gcid",
        [
            OtDataField(
                "struct", "GlyphCIDMapping", description="Glyph to CID mapping table."
            ),
        ],
    ),
    (
        "GlyphCIDMappingFormat0",
        [
            OtDataField(
                "uint16",
                "Format",
                description="Format of the glyph-to-CID mapping table, = 0.",
            ),
            OtDataField(
                "uint16", "DataFormat", description="Currenty unused, set to zero."
            ),
            OtDataField(
                "uint32", "StructLength", description="Size of the table in bytes."
            ),
            OtDataField("uint16", "Registry", description="The registry ID."),
            OtDataField(
                "char64",
                "RegistryName",
                description="The registry name in ASCII; unused bytes should be set to 0.",
            ),
            OtDataField("uint16", "Order", description="The order ID."),
            OtDataField(
                "char64",
                "OrderName",
                description="The order name in ASCII; unused bytes should be set to 0.",
            ),
            OtDataField(
                "uint16", "SupplementVersion", description="The supplement version."
            ),
            OtDataField(
                "GlyphCIDMap",
                "Mapping",
                description="The CIDs for the glyphs in the font, starting with glyph 0. If a glyph does not correspond to a CID in the identified collection, 0xFFFF is used",
            ),
        ],
    ),
    #
    # lcar
    #
    (
        "lcar",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version number of the ligature caret table (0x00010000 for the initial version).",
            ),
            OtDataField(
                "struct", "LigatureCarets", description="Ligature carets table."
            ),
        ],
    ),
    (
        "LigatureCaretsFormat0",
        [
            OtDataField(
                "uint16",
                "Format",
                description="Format of the ligature caret table. Format 0 indicates division points are distances in font units, Format 1 indicates division points are indexes of control points.",
            ),
            OtDataField(
                "AATLookup(LigCaretDistances)",
                "Carets",
                description="Lookup table associating ligature glyphs with their caret positions, in font unit distances.",
            ),
        ],
    ),
    (
        "LigatureCaretsFormat1",
        [
            OtDataField(
                "uint16",
                "Format",
                description="Format of the ligature caret table. Format 0 indicates division points are distances in font units, Format 1 indicates division points are indexes of control points.",
            ),
            OtDataField(
                "AATLookup(LigCaretPoints)",
                "Carets",
                description="Lookup table associating ligature glyphs with their caret positions, as control points.",
            ),
        ],
    ),
    (
        "LigCaretDistances",
        [
            OtDataField(
                "uint16", "DivsionPointCount", description="Number of division points."
            ),
            OtDataField(
                "int16",
                "DivisionPoint",
                repeat="DivsionPointCount",
                aux=0,
                description="Distance in font units through which a subdivision is made orthogonally to the baseline.",
            ),
        ],
    ),
    (
        "LigCaretPoints",
        [
            OtDataField(
                "uint16", "DivsionPointCount", description="Number of division points."
            ),
            OtDataField(
                "int16",
                "DivisionPoint",
                repeat="DivsionPointCount",
                aux=0,
                description="The number of the control point through which a subdivision is made orthogonally to the baseline.",
            ),
        ],
    ),
    #
    # mort
    #
    (
        "mort",
        [
            OtDataField("Version", "Version", description="Version of the mort table."),
            OtDataField(
                "uint32",
                "MorphChainCount",
                description="Number of metamorphosis chains.",
            ),
            OtDataField(
                "MortChain",
                "MorphChain",
                repeat="MorphChainCount",
                aux=0,
                description="Array of metamorphosis chains.",
            ),
        ],
    ),
    (
        "MortChain",
        [
            OtDataField(
                "Flags32",
                "DefaultFlags",
                description="The default specification for subtables.",
            ),
            OtDataField(
                "uint32",
                "StructLength",
                description="Total byte count, including this header; must be a multiple of 4.",
            ),
            OtDataField(
                "uint16",
                "MorphFeatureCount",
                description="Number of metamorphosis feature entries.",
            ),
            OtDataField(
                "uint16",
                "MorphSubtableCount",
                description="The number of subtables in the chain.",
            ),
            OtDataField(
                "struct",
                "MorphFeature",
                repeat="MorphFeatureCount",
                aux=0,
                description="Array of metamorphosis features.",
            ),
            OtDataField(
                "MortSubtable",
                "MorphSubtable",
                repeat="MorphSubtableCount",
                aux=0,
                description="Array of metamorphosis subtables.",
            ),
        ],
    ),
    (
        "MortSubtable",
        [
            OtDataField(
                "uint16",
                "StructLength",
                description="Total subtable length, including this header.",
            ),
            OtDataField(
                "uint8",
                "CoverageFlags",
                description="Most significant byte of coverage flags.",
            ),
            OtDataField("uint8", "MorphType", description="Subtable type."),
            OtDataField(
                "Flags32",
                "SubFeatureFlags",
                description="The 32-bit mask identifying which subtable this is (the subtable being executed if the AND of this value and the processed defaultFlags is nonzero).",
            ),
            OtDataField("SubStruct", "SubStruct", description="SubTable."),
        ],
    ),
    #
    # morx
    #
    (
        "morx",
        [
            OtDataField("uint16", "Version", description="Version of the morx table."),
            OtDataField("uint16", "Reserved", description="Reserved (set to zero)."),
            OtDataField(
                "uint32",
                "MorphChainCount",
                description="Number of extended metamorphosis chains.",
            ),
            OtDataField(
                "MorxChain",
                "MorphChain",
                repeat="MorphChainCount",
                aux=0,
                description="Array of extended metamorphosis chains.",
            ),
        ],
    ),
    (
        "MorxChain",
        [
            OtDataField(
                "Flags32",
                "DefaultFlags",
                description="The default specification for subtables.",
            ),
            OtDataField(
                "uint32",
                "StructLength",
                description="Total byte count, including this header; must be a multiple of 4.",
            ),
            OtDataField(
                "uint32",
                "MorphFeatureCount",
                description="Number of feature subtable entries.",
            ),
            OtDataField(
                "uint32",
                "MorphSubtableCount",
                description="The number of subtables in the chain.",
            ),
            OtDataField(
                "MorphFeature",
                "MorphFeature",
                repeat="MorphFeatureCount",
                aux=0,
                description="Array of metamorphosis features.",
            ),
            OtDataField(
                "MorxSubtable",
                "MorphSubtable",
                repeat="MorphSubtableCount",
                aux=0,
                description="Array of extended metamorphosis subtables.",
            ),
        ],
    ),
    (
        "MorphFeature",
        [
            OtDataField("uint16", "FeatureType", description="The type of feature."),
            OtDataField(
                "uint16",
                "FeatureSetting",
                description="The feature's setting (aka selector).",
            ),
            OtDataField(
                "Flags32",
                "EnableFlags",
                description="Flags for the settings that this feature and setting enables.",
            ),
            OtDataField(
                "Flags32",
                "DisableFlags",
                description="Complement of flags for the settings that this feature and setting disable.",
            ),
        ],
    ),
    # Apple TrueType Reference Manual, chapter “The ‘morx’ table”,
    # section “Metamorphosis Subtables”.
    # https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6morx.html
    (
        "MorxSubtable",
        [
            OtDataField(
                "uint32",
                "StructLength",
                description="Total subtable length, including this header.",
            ),
            OtDataField(
                "uint8",
                "CoverageFlags",
                description="Most significant byte of coverage flags.",
            ),
            OtDataField("uint16", "Reserved", description="Unused."),
            OtDataField("uint8", "MorphType", description="Subtable type."),
            OtDataField(
                "Flags32",
                "SubFeatureFlags",
                description="The 32-bit mask identifying which subtable this is (the subtable being executed if the AND of this value and the processed defaultFlags is nonzero).",
            ),
            OtDataField("SubStruct", "SubStruct", description="SubTable."),
        ],
    ),
    (
        "StateHeader",
        [
            OtDataField(
                "uint32",
                "ClassCount",
                description="Number of classes, which is the number of 16-bit entry indices in a single line in the state array.",
            ),
            OtDataField(
                "uint32",
                "MorphClass",
                description="Offset from the start of this state table header to the start of the class table.",
            ),
            OtDataField(
                "uint32",
                "StateArrayOffset",
                description="Offset from the start of this state table header to the start of the state array.",
            ),
            OtDataField(
                "uint32",
                "EntryTableOffset",
                description="Offset from the start of this state table header to the start of the entry table.",
            ),
        ],
    ),
    (
        "RearrangementMorph",
        [
            OtDataField(
                "STXHeader(RearrangementMorphAction)",
                "StateTable",
                description="Finite-state transducer table for indic rearrangement.",
            ),
        ],
    ),
    (
        "ContextualMorph",
        [
            OtDataField(
                "STXHeader(ContextualMorphAction)",
                "StateTable",
                description="Finite-state transducer for contextual glyph substitution.",
            ),
        ],
    ),
    (
        "LigatureMorph",
        [
            OtDataField(
                "STXHeader(LigatureMorphAction)",
                "StateTable",
                description="Finite-state transducer for ligature substitution.",
            ),
        ],
    ),
    (
        "NoncontextualMorph",
        [
            OtDataField(
                "AATLookup(GlyphID)",
                "Substitution",
                description="The noncontextual glyph substitution table.",
            ),
        ],
    ),
    (
        "InsertionMorph",
        [
            OtDataField(
                "STXHeader(InsertionMorphAction)",
                "StateTable",
                description="Finite-state transducer for glyph insertion.",
            ),
        ],
    ),
    (
        "MorphClass",
        [
            OtDataField(
                "uint16",
                "FirstGlyph",
                description="Glyph index of the first glyph in the class table.",
            ),
            # ('uint16', 'GlyphCount', None, None, 'Number of glyphs in class table.'),
            # ('uint8', 'GlyphClass', 'GlyphCount', 0, 'The class codes (indexed by glyph index minus firstGlyph). Class codes range from 0 to the value of stateSize minus 1.'),
        ],
    ),
    # If the 'morx' table version is 3 or greater, then the last subtable in the chain is followed by a subtableGlyphCoverageArray, as described below.
    # 		('Offset', 'MarkGlyphSetsDef', None, 'round(Version*0x10000) >= 0x00010002', 'Offset to the table of mark set definitions-from beginning of GDEF header (may be NULL)'),
    #
    # prop
    #
    (
        "prop",
        [
            OtDataField(
                "Fixed",
                "Version",
                description="Version number of the AAT glyphs property table. Version 1.0 is the initial table version. Version 2.0, which is recognized by macOS 8.5 and later, adds support for the “attaches on right” bit. Version 3.0, which gets recognized by macOS X and iOS, adds support for the additional directional properties defined in Unicode 3.0.",
            ),
            OtDataField("struct", "GlyphProperties", description="Glyph properties."),
        ],
    ),
    (
        "GlyphPropertiesFormat0",
        [
            OtDataField("uint16", "Format", description="Format, = 0."),
            OtDataField(
                "uint16",
                "DefaultProperties",
                description="Default properties applied to a glyph. Since there is no lookup table in prop format 0, the default properties get applied to every glyph in the font.",
            ),
        ],
    ),
    (
        "GlyphPropertiesFormat1",
        [
            OtDataField("uint16", "Format", description="Format, = 1."),
            OtDataField(
                "uint16",
                "DefaultProperties",
                description="Default properties applied to a glyph if that glyph is not present in the Properties lookup table.",
            ),
            OtDataField(
                "AATLookup(uint16)",
                "Properties",
                description="Lookup data associating glyphs with their properties.",
            ),
        ],
    ),
    #
    # opbd
    #
    (
        "opbd",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version number of the optical bounds table (0x00010000 for the initial version).",
            ),
            OtDataField("struct", "OpticalBounds", description="Optical bounds table."),
        ],
    ),
    (
        "OpticalBoundsFormat0",
        [
            OtDataField(
                "uint16",
                "Format",
                description="Format of the optical bounds table, = 0.",
            ),
            OtDataField(
                "AATLookup(OpticalBoundsDeltas)",
                "OpticalBoundsDeltas",
                description="Lookup table associating glyphs with their optical bounds, given as deltas in font units.",
            ),
        ],
    ),
    (
        "OpticalBoundsFormat1",
        [
            OtDataField(
                "uint16",
                "Format",
                description="Format of the optical bounds table, = 1.",
            ),
            OtDataField(
                "AATLookup(OpticalBoundsPoints)",
                "OpticalBoundsPoints",
                description="Lookup table associating glyphs with their optical bounds, given as references to control points.",
            ),
        ],
    ),
    (
        "OpticalBoundsDeltas",
        [
            OtDataField(
                "int16",
                "Left",
                description="Delta value for the left-side optical edge.",
            ),
            OtDataField(
                "int16", "Top", description="Delta value for the top-side optical edge."
            ),
            OtDataField(
                "int16",
                "Right",
                description="Delta value for the right-side optical edge.",
            ),
            OtDataField(
                "int16",
                "Bottom",
                description="Delta value for the bottom-side optical edge.",
            ),
        ],
    ),
    (
        "OpticalBoundsPoints",
        [
            OtDataField(
                "int16",
                "Left",
                description="Control point index for the left-side optical edge, or -1 if this glyph has none.",
            ),
            OtDataField(
                "int16",
                "Top",
                description="Control point index for the top-side optical edge, or -1 if this glyph has none.",
            ),
            OtDataField(
                "int16",
                "Right",
                description="Control point index for the right-side optical edge, or -1 if this glyph has none.",
            ),
            OtDataField(
                "int16",
                "Bottom",
                description="Control point index for the bottom-side optical edge, or -1 if this glyph has none.",
            ),
        ],
    ),
    #
    # TSIC
    #
    (
        "TSIC",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of table initially set to 0x00010000.",
            ),
            OtDataField("uint16", "Flags", description="TSIC flags - set to 0"),
            OtDataField("uint16", "AxisCount", description="Axis count from fvar"),
            OtDataField("uint16", "RecordCount", description="TSIC record count"),
            OtDataField("uint16", "Reserved", description="Set to 0"),
            OtDataField(
                "Tag",
                "AxisArray",
                repeat="AxisCount",
                aux=0,
                description="Array of axis tags in fvar order",
            ),
            OtDataField(
                "LocationRecord",
                "RecordLocations",
                repeat="RecordCount",
                aux=0,
                description="Location in variation space of TSIC record",
            ),
            OtDataField(
                "TSICRecord",
                "Record",
                repeat="RecordCount",
                aux=0,
                description="Array of TSIC records",
            ),
        ],
    ),
    (
        "LocationRecord",
        [
            OtDataField(
                "F2Dot14", "Axis", repeat="AxisCount", aux=0, description="Axis record"
            ),
        ],
    ),
    (
        "TSICRecord",
        [
            OtDataField("uint16", "Flags", description="Record flags - set to 0"),
            OtDataField(
                "uint16",
                "NumCVTEntries",
                description="Number of CVT number value pairs",
            ),
            OtDataField(
                "uint16",
                "NameLength",
                description="Length of optional user record name",
            ),
            OtDataField(
                "uint16",
                "NameArray",
                repeat="NameLength",
                aux=0,
                description="Unicode 16 name",
            ),
            OtDataField(
                "uint16",
                "CVTArray",
                repeat="NumCVTEntries",
                aux=0,
                description="CVT number array",
            ),
            OtDataField(
                "int16",
                "CVTValueArray",
                repeat="NumCVTEntries",
                aux=0,
                description="CVT value",
            ),
        ],
    ),
    #
    # COLR
    #
    (
        "COLR",
        [
            OtDataField(
                "uint16", "Version", description="Table version number (starts at 0)."
            ),
            OtDataField(
                "uint16",
                "BaseGlyphRecordCount",
                description="Number of Base Glyph Records.",
            ),
            OtDataField(
                "LOffset",
                "BaseGlyphRecordArray",
                description="Offset (from beginning of COLR table) to Base Glyph records.",
            ),
            OtDataField(
                "LOffset",
                "LayerRecordArray",
                description="Offset (from beginning of COLR table) to Layer Records.",
            ),
            OtDataField(
                "uint16", "LayerRecordCount", description="Number of Layer Records."
            ),
            OtDataField(
                "LOffset",
                "BaseGlyphList",
                aux="Version >= 1",
                description="Offset (from beginning of COLR table) to array of Version-1 Base Glyph records.",
            ),
            OtDataField(
                "LOffset",
                "LayerList",
                aux="Version >= 1",
                description="Offset (from beginning of COLR table) to LayerList.",
            ),
            OtDataField(
                "LOffset",
                "ClipList",
                aux="Version >= 1",
                description="Offset to ClipList table (may be NULL)",
            ),
            OtDataField(
                "LOffsetTo(DeltaSetIndexMap)",
                "VarIndexMap",
                aux="Version >= 1",
                description="Offset to DeltaSetIndexMap table (may be NULL)",
            ),
            OtDataField(
                "LOffset",
                "VarStore",
                aux="Version >= 1",
                description="Offset to variation store (may be NULL)",
            ),
        ],
    ),
    (
        "BaseGlyphRecordArray",
        [
            OtDataField(
                "BaseGlyphRecord",
                "BaseGlyphRecord",
                repeat="BaseGlyphRecordCount",
                aux=0,
                description="Base Glyph records.",
            ),
        ],
    ),
    (
        "BaseGlyphRecord",
        [
            OtDataField(
                "GlyphID",
                "BaseGlyph",
                description="Glyph ID of reference glyph. This glyph is for reference only and is not rendered for color.",
            ),
            OtDataField(
                "uint16",
                "FirstLayerIndex",
                description="Index (from beginning of the Layer Records) to the layer record. There will be numLayers consecutive entries for this base glyph.",
            ),
            OtDataField(
                "uint16",
                "NumLayers",
                description="Number of color layers associated with this glyph.",
            ),
        ],
    ),
    (
        "LayerRecordArray",
        [
            OtDataField(
                "LayerRecord",
                "LayerRecord",
                repeat="LayerRecordCount",
                aux=0,
                description="Layer records.",
            ),
        ],
    ),
    (
        "LayerRecord",
        [
            OtDataField(
                "GlyphID",
                "LayerGlyph",
                description="Glyph ID of layer glyph (must be in z-order from bottom to top).",
            ),
            OtDataField(
                "uint16",
                "PaletteIndex",
                description="Index value to use with a selected color palette.",
            ),
        ],
    ),
    (
        "BaseGlyphList",
        [
            OtDataField(
                "uint32",
                "BaseGlyphCount",
                description="Number of Version-1 Base Glyph records",
            ),
            OtDataField(
                "struct",
                "BaseGlyphPaintRecord",
                repeat="BaseGlyphCount",
                aux=0,
                description="Array of Version-1 Base Glyph records",
            ),
        ],
    ),
    (
        "BaseGlyphPaintRecord",
        [
            OtDataField(
                "GlyphID", "BaseGlyph", description="Glyph ID of reference glyph."
            ),
            OtDataField(
                "LOffset",
                "Paint",
                description="Offset (from beginning of BaseGlyphPaintRecord) to Paint, typically a PaintColrLayers.",
            ),
        ],
    ),
    (
        "LayerList",
        [
            OtDataField(
                "uint32", "LayerCount", description="Number of Version-1 Layers"
            ),
            OtDataField(
                "LOffset",
                "Paint",
                repeat="LayerCount",
                aux=0,
                description="Array of offsets to Paint tables, from the start of the LayerList table.",
            ),
        ],
    ),
    (
        "ClipListFormat1",
        [
            OtDataField(
                "uint8",
                "Format",
                description="Format for ClipList with 16bit glyph IDs: 1",
            ),
            OtDataField("uint32", "ClipCount", description="Number of Clip records."),
            OtDataField(
                "struct",
                "ClipRecord",
                repeat="ClipCount",
                aux=0,
                description="Array of Clip records sorted by glyph ID.",
            ),
        ],
    ),
    (
        "ClipRecord",
        [
            OtDataField(
                "uint16", "StartGlyphID", description="First glyph ID in the range."
            ),
            OtDataField(
                "uint16", "EndGlyphID", description="Last glyph ID in the range."
            ),
            OtDataField(
                "Offset24", "ClipBox", description="Offset to a ClipBox table."
            ),
        ],
    ),
    (
        "ClipBoxFormat1",
        [
            OtDataField(
                "uint8",
                "Format",
                description="Format for ClipBox without variation: set to 1.",
            ),
            OtDataField("int16", "xMin", description="Minimum x of clip box."),
            OtDataField("int16", "yMin", description="Minimum y of clip box."),
            OtDataField("int16", "xMax", description="Maximum x of clip box."),
            OtDataField("int16", "yMax", description="Maximum y of clip box."),
        ],
    ),
    (
        "ClipBoxFormat2",
        [
            OtDataField(
                "uint8", "Format", description="Format for variable ClipBox: set to 2."
            ),
            OtDataField(
                "int16", "xMin", description="Minimum x of clip box. VarIndexBase + 0."
            ),
            OtDataField(
                "int16", "yMin", description="Minimum y of clip box. VarIndexBase + 1."
            ),
            OtDataField(
                "int16", "xMax", description="Maximum x of clip box. VarIndexBase + 2."
            ),
            OtDataField(
                "int16", "yMax", description="Maximum y of clip box. VarIndexBase + 3."
            ),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # COLRv1 Affine2x3 uses the same column-major order to serialize a 2D
    # Affine Transformation as the one used by fontTools.misc.transform.
    # However, for historical reasons, the labels 'xy' and 'yx' are swapped.
    # Their fundamental meaning is the same though.
    # COLRv1 Affine2x3 follows the names found in FreeType and Cairo.
    # In all case, the second element in the 6-tuple correspond to the
    # y-part of the x basis vector, and the third to the x-part of the y
    # basis vector.
    # See https://github.com/googlefonts/colr-gradients-spec/pull/85
    (
        "Affine2x3",
        [
            OtDataField("Fixed", "xx", description="x-part of x basis vector"),
            OtDataField("Fixed", "yx", description="y-part of x basis vector"),
            OtDataField("Fixed", "xy", description="x-part of y basis vector"),
            OtDataField("Fixed", "yy", description="y-part of y basis vector"),
            OtDataField("Fixed", "dx", description="Translation in x direction"),
            OtDataField("Fixed", "dy", description="Translation in y direction"),
        ],
    ),
    (
        "VarAffine2x3",
        [
            OtDataField(
                "Fixed", "xx", description="x-part of x basis vector. VarIndexBase + 0."
            ),
            OtDataField(
                "Fixed", "yx", description="y-part of x basis vector. VarIndexBase + 1."
            ),
            OtDataField(
                "Fixed", "xy", description="x-part of y basis vector. VarIndexBase + 2."
            ),
            OtDataField(
                "Fixed", "yy", description="y-part of y basis vector. VarIndexBase + 3."
            ),
            OtDataField(
                "Fixed",
                "dx",
                description="Translation in x direction. VarIndexBase + 4.",
            ),
            OtDataField(
                "Fixed",
                "dy",
                description="Translation in y direction. VarIndexBase + 5.",
            ),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    (
        "ColorStop",
        [
            OtDataField("F2Dot14", "StopOffset"),
            OtDataField(
                "uint16", "PaletteIndex", description="Index for a CPAL palette entry."
            ),
            OtDataField(
                "F2Dot14", "Alpha", description="Values outsided [0.,1.] reserved"
            ),
        ],
    ),
    (
        "VarColorStop",
        [
            OtDataField("F2Dot14", "StopOffset", description="VarIndexBase + 0."),
            OtDataField(
                "uint16", "PaletteIndex", description="Index for a CPAL palette entry."
            ),
            OtDataField(
                "F2Dot14",
                "Alpha",
                description="Values outsided [0.,1.] reserved. VarIndexBase + 1.",
            ),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    (
        "ColorLine",
        [
            OtDataField(
                "ExtendMode",
                "Extend",
                description="Enum {PAD = 0, REPEAT = 1, REFLECT = 2}",
            ),
            OtDataField("uint16", "StopCount", description="Number of Color stops."),
            OtDataField(
                "ColorStop",
                "ColorStop",
                repeat="StopCount",
                aux=0,
                description="Array of Color stops.",
            ),
        ],
    ),
    (
        "VarColorLine",
        [
            OtDataField(
                "ExtendMode",
                "Extend",
                description="Enum {PAD = 0, REPEAT = 1, REFLECT = 2}",
            ),
            OtDataField("uint16", "StopCount", description="Number of Color stops."),
            OtDataField(
                "VarColorStop",
                "ColorStop",
                repeat="StopCount",
                aux=0,
                description="Array of Color stops.",
            ),
        ],
    ),
    # PaintColrLayers
    (
        "PaintFormat1",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 1"
            ),
            OtDataField(
                "uint8",
                "NumLayers",
                description="Number of offsets to Paint to read from LayerList.",
            ),
            OtDataField(
                "uint32", "FirstLayerIndex", description="Index into LayerList."
            ),
        ],
    ),
    # PaintSolid
    (
        "PaintFormat2",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 2"
            ),
            OtDataField(
                "uint16", "PaletteIndex", description="Index for a CPAL palette entry."
            ),
            OtDataField(
                "F2Dot14", "Alpha", description="Values outsided [0.,1.] reserved"
            ),
        ],
    ),
    # PaintVarSolid
    (
        "PaintFormat3",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 3"
            ),
            OtDataField(
                "uint16", "PaletteIndex", description="Index for a CPAL palette entry."
            ),
            OtDataField(
                "F2Dot14",
                "Alpha",
                description="Values outsided [0.,1.] reserved. VarIndexBase + 0.",
            ),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintLinearGradient
    (
        "PaintFormat4",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 4"
            ),
            OtDataField(
                "Offset24",
                "ColorLine",
                description="Offset (from beginning of PaintLinearGradient table) to ColorLine subtable.",
            ),
            OtDataField("int16", "x0"),
            OtDataField("int16", "y0"),
            OtDataField("int16", "x1"),
            OtDataField("int16", "y1"),
            OtDataField("int16", "x2"),
            OtDataField("int16", "y2"),
        ],
    ),
    # PaintVarLinearGradient
    (
        "PaintFormat5",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 5"
            ),
            OtDataField(
                "LOffset24To(VarColorLine)",
                "ColorLine",
                description="Offset (from beginning of PaintVarLinearGradient table) to VarColorLine subtable.",
            ),
            OtDataField("int16", "x0", description="VarIndexBase + 0."),
            OtDataField("int16", "y0", description="VarIndexBase + 1."),
            OtDataField("int16", "x1", description="VarIndexBase + 2."),
            OtDataField("int16", "y1", description="VarIndexBase + 3."),
            OtDataField("int16", "x2", description="VarIndexBase + 4."),
            OtDataField("int16", "y2", description="VarIndexBase + 5."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintRadialGradient
    (
        "PaintFormat6",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 6"
            ),
            OtDataField(
                "Offset24",
                "ColorLine",
                description="Offset (from beginning of PaintRadialGradient table) to ColorLine subtable.",
            ),
            OtDataField("int16", "x0"),
            OtDataField("int16", "y0"),
            OtDataField("uint16", "r0"),
            OtDataField("int16", "x1"),
            OtDataField("int16", "y1"),
            OtDataField("uint16", "r1"),
        ],
    ),
    # PaintVarRadialGradient
    (
        "PaintFormat7",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 7"
            ),
            OtDataField(
                "LOffset24To(VarColorLine)",
                "ColorLine",
                description="Offset (from beginning of PaintVarRadialGradient table) to VarColorLine subtable.",
            ),
            OtDataField("int16", "x0", description="VarIndexBase + 0."),
            OtDataField("int16", "y0", description="VarIndexBase + 1."),
            OtDataField("uint16", "r0", description="VarIndexBase + 2."),
            OtDataField("int16", "x1", description="VarIndexBase + 3."),
            OtDataField("int16", "y1", description="VarIndexBase + 4."),
            OtDataField("uint16", "r1", description="VarIndexBase + 5."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintSweepGradient
    (
        "PaintFormat8",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 8"
            ),
            OtDataField(
                "Offset24",
                "ColorLine",
                description="Offset (from beginning of PaintSweepGradient table) to ColorLine subtable.",
            ),
            OtDataField("int16", "centerX", description="Center x coordinate."),
            OtDataField("int16", "centerY", description="Center y coordinate."),
            OtDataField(
                "BiasedAngle",
                "startAngle",
                description="Start of the angular range of the gradient.",
            ),
            OtDataField(
                "BiasedAngle",
                "endAngle",
                description="End of the angular range of the gradient.",
            ),
        ],
    ),
    # PaintVarSweepGradient
    (
        "PaintFormat9",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 9"
            ),
            OtDataField(
                "LOffset24To(VarColorLine)",
                "ColorLine",
                description="Offset (from beginning of PaintVarSweepGradient table) to VarColorLine subtable.",
            ),
            OtDataField(
                "int16", "centerX", description="Center x coordinate. VarIndexBase + 0."
            ),
            OtDataField(
                "int16", "centerY", description="Center y coordinate. VarIndexBase + 1."
            ),
            OtDataField(
                "BiasedAngle",
                "startAngle",
                description="Start of the angular range of the gradient. VarIndexBase + 2.",
            ),
            OtDataField(
                "BiasedAngle",
                "endAngle",
                description="End of the angular range of the gradient. VarIndexBase + 3.",
            ),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintGlyph
    (
        "PaintFormat10",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 10"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintGlyph table) to Paint subtable.",
            ),
            OtDataField(
                "GlyphID", "Glyph", description="Glyph ID for the source outline."
            ),
        ],
    ),
    # PaintColrGlyph
    (
        "PaintFormat11",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 11"
            ),
            OtDataField(
                "GlyphID",
                "Glyph",
                description="Virtual glyph ID for a BaseGlyphList base glyph.",
            ),
        ],
    ),
    # PaintTransform
    (
        "PaintFormat12",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 12"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintTransform table) to Paint subtable.",
            ),
            OtDataField(
                "LOffset24To(Affine2x3)",
                "Transform",
                description="2x3 matrix for 2D affine transformations.",
            ),
        ],
    ),
    # PaintVarTransform
    (
        "PaintFormat13",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 13"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarTransform table) to Paint subtable.",
            ),
            OtDataField(
                "LOffset24To(VarAffine2x3)",
                "Transform",
                description="2x3 matrix for 2D affine transformations.",
            ),
        ],
    ),
    # PaintTranslate
    (
        "PaintFormat14",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 14"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintTranslate table) to Paint subtable.",
            ),
            OtDataField("int16", "dx", description="Translation in x direction."),
            OtDataField("int16", "dy", description="Translation in y direction."),
        ],
    ),
    # PaintVarTranslate
    (
        "PaintFormat15",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 15"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarTranslate table) to Paint subtable.",
            ),
            OtDataField(
                "int16",
                "dx",
                description="Translation in x direction. VarIndexBase + 0.",
            ),
            OtDataField(
                "int16",
                "dy",
                description="Translation in y direction. VarIndexBase + 1.",
            ),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintScale
    (
        "PaintFormat16",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 16"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintScale table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scaleX"),
            OtDataField("F2Dot14", "scaleY"),
        ],
    ),
    # PaintVarScale
    (
        "PaintFormat17",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 17"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarScale table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scaleX", description="VarIndexBase + 0."),
            OtDataField("F2Dot14", "scaleY", description="VarIndexBase + 1."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintScaleAroundCenter
    (
        "PaintFormat18",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 18"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintScaleAroundCenter table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scaleX"),
            OtDataField("F2Dot14", "scaleY"),
            OtDataField("int16", "centerX"),
            OtDataField("int16", "centerY"),
        ],
    ),
    # PaintVarScaleAroundCenter
    (
        "PaintFormat19",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 19"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarScaleAroundCenter table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scaleX", description="VarIndexBase + 0."),
            OtDataField("F2Dot14", "scaleY", description="VarIndexBase + 1."),
            OtDataField("int16", "centerX", description="VarIndexBase + 2."),
            OtDataField("int16", "centerY", description="VarIndexBase + 3."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintScaleUniform
    (
        "PaintFormat20",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 20"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintScaleUniform table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scale"),
        ],
    ),
    # PaintVarScaleUniform
    (
        "PaintFormat21",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 21"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarScaleUniform table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scale", description="VarIndexBase + 0."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintScaleUniformAroundCenter
    (
        "PaintFormat22",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 22"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintScaleUniformAroundCenter table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scale"),
            OtDataField("int16", "centerX"),
            OtDataField("int16", "centerY"),
        ],
    ),
    # PaintVarScaleUniformAroundCenter
    (
        "PaintFormat23",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 23"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarScaleUniformAroundCenter table) to Paint subtable.",
            ),
            OtDataField("F2Dot14", "scale", description="VarIndexBase + 0"),
            OtDataField("int16", "centerX", description="VarIndexBase + 1"),
            OtDataField("int16", "centerY", description="VarIndexBase + 2"),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintRotate
    (
        "PaintFormat24",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 24"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintRotate table) to Paint subtable.",
            ),
            OtDataField("Angle", "angle"),
        ],
    ),
    # PaintVarRotate
    (
        "PaintFormat25",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 25"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarRotate table) to Paint subtable.",
            ),
            OtDataField("Angle", "angle", description="VarIndexBase + 0."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintRotateAroundCenter
    (
        "PaintFormat26",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 26"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintRotateAroundCenter table) to Paint subtable.",
            ),
            OtDataField("Angle", "angle"),
            OtDataField("int16", "centerX"),
            OtDataField("int16", "centerY"),
        ],
    ),
    # PaintVarRotateAroundCenter
    (
        "PaintFormat27",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 27"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarRotateAroundCenter table) to Paint subtable.",
            ),
            OtDataField("Angle", "angle", description="VarIndexBase + 0."),
            OtDataField("int16", "centerX", description="VarIndexBase + 1."),
            OtDataField("int16", "centerY", description="VarIndexBase + 2."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintSkew
    (
        "PaintFormat28",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 28"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintSkew table) to Paint subtable.",
            ),
            OtDataField("Angle", "xSkewAngle"),
            OtDataField("Angle", "ySkewAngle"),
        ],
    ),
    # PaintVarSkew
    (
        "PaintFormat29",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 29"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarSkew table) to Paint subtable.",
            ),
            OtDataField("Angle", "xSkewAngle", description="VarIndexBase + 0."),
            OtDataField("Angle", "ySkewAngle", description="VarIndexBase + 1."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintSkewAroundCenter
    (
        "PaintFormat30",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 30"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintSkewAroundCenter table) to Paint subtable.",
            ),
            OtDataField("Angle", "xSkewAngle"),
            OtDataField("Angle", "ySkewAngle"),
            OtDataField("int16", "centerX"),
            OtDataField("int16", "centerY"),
        ],
    ),
    # PaintVarSkewAroundCenter
    (
        "PaintFormat31",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 31"
            ),
            OtDataField(
                "Offset24",
                "Paint",
                description="Offset (from beginning of PaintVarSkewAroundCenter table) to Paint subtable.",
            ),
            OtDataField("Angle", "xSkewAngle", description="VarIndexBase + 0."),
            OtDataField("Angle", "ySkewAngle", description="VarIndexBase + 1."),
            OtDataField("int16", "centerX", description="VarIndexBase + 2."),
            OtDataField("int16", "centerY", description="VarIndexBase + 3."),
            OtDataField(
                "VarIndex",
                "VarIndexBase",
                description="Base index into DeltaSetIndexMap.",
            ),
        ],
    ),
    # PaintComposite
    (
        "PaintFormat32",
        [
            OtDataField(
                "uint8", "PaintFormat", description="Format identifier-format = 32"
            ),
            OtDataField(
                "LOffset24To(Paint)",
                "SourcePaint",
                description="Offset (from beginning of PaintComposite table) to source Paint subtable.",
            ),
            OtDataField(
                "CompositeMode",
                "CompositeMode",
                description="A CompositeMode enumeration value.",
            ),
            OtDataField(
                "LOffset24To(Paint)",
                "BackdropPaint",
                description="Offset (from beginning of PaintComposite table) to backdrop Paint subtable.",
            ),
        ],
    ),
    #
    # avar
    #
    (
        "AxisValueMap",
        [
            OtDataField(
                "F2Dot14",
                "FromCoordinate",
                description="A normalized coordinate value obtained using default normalization",
            ),
            OtDataField(
                "F2Dot14",
                "ToCoordinate",
                description="The modified, normalized coordinate value",
            ),
        ],
    ),
    (
        "AxisSegmentMap",
        [
            OtDataField(
                "uint16",
                "PositionMapCount",
                description="The number of correspondence pairs for this axis",
            ),
            OtDataField(
                "AxisValueMap",
                "AxisValueMap",
                repeat="PositionMapCount",
                aux=0,
                description="The array of axis value map records for this axis",
            ),
        ],
    ),
    (
        "avar",
        [
            OtDataField(
                "Version",
                "Version",
                description="Version of the avar table- 0x00010000 or 0x00020000",
            ),
            OtDataField(
                "uint16", "Reserved", description="Permanently reserved; set to zero"
            ),
            OtDataField(
                "uint16",
                "AxisCount",
                description='The number of variation axes for this font. This must be the same number as axisCount in the "fvar" table',
            ),
            OtDataField(
                "AxisSegmentMap",
                "AxisSegmentMap",
                repeat="AxisCount",
                aux=0,
                description='The segment maps array — one segment map for each axis, in the order of axes specified in the "fvar" table',
            ),
            OtDataField(
                "LOffsetTo(DeltaSetIndexMap)", "VarIdxMap", aux="Version >= 0x00020000"
            ),
            OtDataField("LOffset", "VarStore", aux="Version >= 0x00020000"),
        ],
    ),
    #
    # IFT - Incremental Font Transfer tables
    # https://w3c.github.io/IFT/Overview.html
    # Reference: https://github.com/googlefonts/fontations/blob/main/read-fonts/src/tables/ift.rs
    #
    (
        "PatchMapFormat2",
        [
            OtDataField(
                "uint8", "Format", description="Set to 2, identifies this as format 2."
            ),
            OtDataField("uint24", "Reserved", description="Not used, set to 0."),
            OtDataField(
                "uint8",
                "Flags",
                description="Bit 0: CffCharStringsOffset present. Bit 1: Cff2CharStringsOffset present.",
            ),
            OtDataField(
                "uint32",
                "CompatibilityId",
                repeat=4,
                aux=0,
                description="Unique ID to identify compatible patches (16 bytes).",
            ),
            OtDataField(
                "uint8",
                "DefaultPatchFormat",
                description="Default format of patches linked to by urlTemplate.",
            ),
            OtDataField(
                "uint24",
                "NumEntries",
                description="Number of entries encoded in this table.",
            ),
            OtDataField(
                "LOffset",
                "MappingEntries",
                description="Offset to a MappingEntries sub-table.",
            ),
            OtDataField(
                "LOffset",
                "EntryIdStringData",
                description="Offset to entry ID string data block. May be null (0).",
            ),
            OtDataField(
                "uint16",
                "UrlTemplateLength",
                description="Length of the urlTemplate byte array.",
            ),
            OtDataField(
                "uint8",
                "UrlTemplate",
                repeat="UrlTemplateLength",
                aux=0,
                description="URL Template bytes used to produce URL strings for each entry.",
            ),
            OtDataField(
                "uint32",
                "CffCharStringsOffset",
                aux="Flags & 0x01",
                description="Offset from start of CFF table to CharStrings INDEX.",
            ),
            OtDataField(
                "uint32",
                "Cff2CharStringsOffset",
                aux="Flags & 0x02",
                description="Offset from start of CFF2 table to CharStrings INDEX.",
            ),
        ],
    ),
    # 'MappingEntries' contains stateful, delta-encoded entry IDs.  The custom
    # 'MappingEntriesConverter' is used to do a stateful parsing of all records.
    (
        "MappingEntries",
        [
            OtDataField(
                "MappingEntries",
                "entries",
                description="Array of MappingEntry records.",
            )
        ],
    ),
    ("EntryIdStringData", []),
]
