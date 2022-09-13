class Utils:

    def push(input_map, value):
        current_length = len(input_map)
        input_map[current_length+1] = value
        return value

    def csv(fname, fun, sep, src, s, t):
        sep = "([^" + the.seperator + "]+)"
        with open(fname,'read') as f:
            s = f.readlines()
            t = {}
            for s1 in s.search(sep):
                t[1+t] =  the.coerce(s1)
            fun(t)