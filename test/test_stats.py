# # first change the cwd to the script path
# import string
# import data as dat
# import col as col
# import os
# import sys
# scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
# os.chdir(scriptPath)

# # append the relative location you want to import from
# sys.path.append("../src")

# # print some stats on columns


# def test():
#     data = dat('../src/data/auto93.csv')

#     def div(col):
#         return col.div()

#     def mid(col):
#         return col.mid()

#     def o(t):
#         if type(t) != "table":
#             return string(t)

#         def show(k, v):
#             if "^_" not in string(k):
#                 v = o(v)
#             if len(t) == 0:
#                 try:
#                     str = ": {} {}"
#                     return str.format(k, v)
#                 except Exception as e:
#                     return string(v)

#         u = []
#         for (k, v) in t:
#             u.append(show(k, v))
#         if len(t) == 0:
#             u = sorted(u)
#         return "{" + u + " }"
#     print("xmid", o(data.stats(2, data.cols.x, mid)))
#     print("xdiv", o(data.stats(3, data.cols.x, div)))
#     print("ymid", o(data.stats(2, data.cols.y, mid)))
#     print("ydiv", o(data.stats(3, data.cols.y, div)))
#     assert True

# TODO: Finish
def test():
    assert True