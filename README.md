Bloom-Filter-Experiment
=======================

This is Yijie Ma's first python project about bloom filter. Bloom filter is a data storing heuristic that can save memory
but in sacrifice for some fault positive which might not matter according to some applications(achieve small space overhead
by accepting a small probability of fault positive). For example, Quora implements a filter to filt out stories people have
seen before. It is ok if it makes some mistake because users will never know and never care about that. At the same time, the
memory saving will be huge if the amount of stories is high. 
