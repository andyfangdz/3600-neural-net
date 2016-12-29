import Testing as t
import sys

print "Generated with the following Python version:\n" + sys.version + "\n\n"

slim_report_template = "Max: %f, Average: %f, Stddev: %f"

report_template = """\
=============%s=============
""" + slim_report_template + """
============================
"""

# Q5


accs = [t.testPenData()[-1] for _ in range(5)]

print(report_template % (
    "testPenData()",
    max(accs),
    t.average(accs),
    t.stDeviation(accs)
))

accs = [t.testCarData()[-1] for _ in range(5)]

print(report_template % (
    "testCarData()",
    max(accs),
    t.average(accs),
    t.stDeviation(accs)
))

# Q6

print """\
| Perceptrons  | Car Data Accuracy | Pen Data Accuracy |
| ------------ | ----------------- | ----------------- |\
"""

results = []
for p in range(0, 41, 5):
    acc_cars = [t.testCarData([p])[-1] for _ in range(5)]
    acc_pens = [t.testPenData([p])[-1] for _ in range(5)]
    print "|%d|%s|%s|" % (p,
                          slim_report_template % (max(acc_cars),
                                                  t.average(acc_cars),
                                                  t.stDeviation(acc_cars)),
                          slim_report_template % (max(acc_pens),
                                                  t.average(acc_pens),
                                                  t.stDeviation(acc_pens)))
    results.append((p, t.average(acc_cars), t.average(acc_pens)))
