from nose.tools import *
from BLOOM_FILTER.bloomfilter import BloomFilter

def test_basic_bloomfilter():
	bf = BloomFilter(1000, 5)
	assert_equal(bf.size, 1000)
	assert_equal(bf.hash_count, 5)

def test_200000_bloomfilter():
	bf = BloomFilter(200000, 1)
	lines = open("/Users/yijiem/Desktop/python_project/bloom_filter/words").read().splitlines();
	for line in lines:
		bf.add(line)
	print "running 200000 test"
	print "google" + " " + bf.lookup("google")
	print "max" + " " + bf.lookup("max")
	print "zksjnlkjnlbjnasldn" + " " + bf.lookup("zksjnlkjnlbjnasldn")
        print "123" + " " + bf.lookup("123")
        print ""

def test_300000_bloomfilter():
        bf = BloomFilter(300000, 1)
        lines = open("/Users/yijiem/Desktop/python_project/bloom_filter/words").read().splitlines();
        for line in lines:
                bf.add(line)
        print "running 300000 test"
        print "google" + " " + bf.lookup("google")
        print "max" + " " + bf.lookup("max")
        print "zksjnlkjnlbjnasldn" + " " + bf.lookup("zksjnlkjnlbjnasldn")
        print "123" + " " + bf.lookup("123")
	print ""

def test_400000_bloomfilter():
        bf = BloomFilter(400000, 2)
        lines = open("/Users/yijiem/Desktop/python_project/bloom_filter/words").read().splitlines();
        for line in lines:
                bf.add(line)
        print "running 400000 test"
        print "google" + " " + bf.lookup("google")
        print "max" + " " + bf.lookup("max")
        print "zksjnlkjnlbjnasldn" + " " + bf.lookup("zksjnlkjnlbjnasldn")
        print "123" + " " + bf.lookup("123")
	print ""

def test_optimal_bloomfilter():
        bf = BloomFilter(700000, 3)
        lines = open("/Users/yijiem/Desktop/python_project/bloom_filter/words").read().splitlines();
        for line in lines:
                bf.add(line)
        print "running optimal test"
        print "google" + " " + bf.lookup("google")
        print "max" + " " + bf.lookup("max")
        print "zksjnlkjnlbjnasldn" + " " + bf.lookup("zksjnlkjnlbjnasldn")
        print "123" + " " + bf.lookup("123")
        print ""
