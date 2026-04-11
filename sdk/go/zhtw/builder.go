package zhtw

// Builder constructs a custom Converter with non-default settings.
type Builder struct {
	sources       []Source
	customDict    map[string]string
	ambiguityMode AmbiguityMode
}

// NewBuilder returns a Builder with default settings (Cn+Hk, Strict).
func NewBuilder() *Builder {
	return &Builder{
		sources:       []Source{SourceCn, SourceHk},
		ambiguityMode: AmbiguityStrict,
	}
}

// Sources sets the dictionary sources. Default: [SourceCn, SourceHk].
func (b *Builder) Sources(sources ...Source) *Builder {
	b.sources = sources
	return b
}

// CustomDict sets user overrides that take priority over built-in terms.
func (b *Builder) CustomDict(dict map[string]string) *Builder {
	b.customDict = dict
	return b
}

// SetAmbiguityMode sets the ambiguity handling mode. Default: AmbiguityStrict.
func (b *Builder) SetAmbiguityMode(mode AmbiguityMode) *Builder {
	b.ambiguityMode = mode
	return b
}

// Build creates the Converter. Returns an error if sources is empty.
func (b *Builder) Build() (*Converter, error) {
	data := getParsedData()
	return buildConverter(data, b.sources, b.customDict, b.ambiguityMode)
}
