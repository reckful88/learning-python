try:
	print 'Lets try ...'
    	r = 1 / 0
    	print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

