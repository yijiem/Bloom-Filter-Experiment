Bloom-Filter-Experiment
=======================

This is Yijie Ma's project about bloom filter implementing using python. Bloom filter is a data storing heuristic that can save memory
but in sacrifice for some fault positive which might not matter according to some applications(achieve small space overhead
by accepting a small probability of fault positive). For example, Quora implements a filter to filt out stories people have
seen before. It is ok if it makes some mistake because users will never know and never care about that. At the same time, the
memory saving will be huge if the amount of stories is high. 

In my experiment, I used mmh3(MurmurHash3 detail will be given) as my hash function and for data sets I used Webster's Second 
International dictionary stored as /usr/share/dict/words in any FreeBSD based operating system I think...

Accuracy Test:
I runned multiple tests based on different m(number of bits).
The number of hash functions is given by the optimal axiom: k = ln(2)* (m/n)  

n(number of words) is always 235886 according to the dictionary  
m(number of bits) = 200000  
k(number of hash functions) = 1  

Query | Output | Result
----- | ------ | ------
"google" | Probably | false positive
"max" | Probably | true
"llsdnln" | Probably | false positive
"123" | Probably | false positive

m = 300000  
k = 1  

 Query | Output | Result
 ----- | ------ | ------
"google" | No | true
"max" | Probably | true
"llsdnln" | No | true
"123" | Probably | false positive

There is someting really interesting in these 3 tests. The first one is obviously a trivial one, because the number of bits is
less than the number of data. So the fault positive rate is high. The second is pretty nice, it has 300000/235886=1.27bit/data
and the outcome is acceptable. Therefore, for a given data set, the more the bit number is the less the fault positive rate.
But, we should never forget that the key about using bloom filter is memory saving. The dictionary we used will take 300kb to store if we choose m to 300000. If we store it into a normal set, assume the average number of bytes for a word is 8, then it
will take 235886 * 8bytes = 1887kb memory, 6 times of bloom filter. As we can imagine, as the number of data becomes larger,
the memory saving of bloom filter will become more salient.

Efficiency Test:

Murmurhash3:  
murmurhash is a hash function created by Austin Appleby in 2008. The current version is murmurhash3. Here is the 32-bits version of murmurhash3:
```c++
void MurmurHash3_x86_32 ( const void * key, int len,
                          uint32_t seed, void * out )
{
  const uint8_t * data = (const uint8_t*)key;
  const int nblocks = len / 4;

  uint32_t h1 = seed;

  const uint32_t c1 = 0xcc9e2d51;
  const uint32_t c2 = 0x1b873593;

  //----------
  // body

  const uint32_t * blocks = (const uint32_t *)(data + nblocks*4);

  for(int i = -nblocks; i; i++)
  {
    uint32_t k1 = getblock32(blocks,i);

    k1 *= c1;
    k1 = ROTL32(k1,15);
    k1 *= c2;

    h1 ^= k1;
    h1 = ROTL32(h1,13);
    h1 = h1*5+0xe6546b64;
  }

  //----------
  // tail

  const uint8_t * tail = (const uint8_t*)(data + nblocks*4);

  uint32_t k1 = 0;

  switch(len & 3)
  {
  case 3: k1 ^= tail[2] << 16;
  case 2: k1 ^= tail[1] << 8;
  case 1: k1 ^= tail[0];
          k1 *= c1; k1 = ROTL32(k1,15); k1 *= c2; h1 ^= k1;
  };

  //----------
  // finalization

  h1 ^= len;

  h1 = fmix32(h1);

  *(uint32_t*)out = h1;
}
```

It processes the input string one character by one, doing some sum, multiply, rotating, and XOR operation and finally mix all values together.

