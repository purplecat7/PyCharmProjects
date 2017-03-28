# define function which creates a new type with attributes given as arg1
def enum(**enums):
    return type('Enum', (), enums)


# creation
m_covg_coll_nodes = enum(domain="domainType", params="parameters",
                         the_ref="referencing", covgs="coverages")
m_covg_nodes = enum(domain="domain", params="parameters",
                    ranges="ranges", range_alt="rangeAlternates")

# iteration over attributes
for item in [a for a in dir(m_covg_nodes) if not a.startswith('__')]:
    print item

    # can't work out how to get the value of each though...
