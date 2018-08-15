from Deployment.Client.client import Client
from multiprocessing import Process
import time
import matplotlib.pyplot as plt


def test_setup(number_of_devices):

    # Setting up a client device
    client = Client(device_type='test_device',
                    seed='',
                    device_name='test',
                    iota_node="http://localhost:14700",
                    route_pow=False)

    # Send a zero value transaction to attach address to tangle
    client.post_to_tangle(data='')

"""
complete_times = []
processes = []
results = []

for i in range(0, 10):

    times = []
    processes = []

    for j in range(0, 50):
        p = Process(target=test_setup, args=())
        processes.append(p)

    for process in processes:

        start = time.time()

        process.start()
        process.join()

        end = time.time()
        elapsed_time = end - start
        times.append(elapsed_time)

        average = sum(times) / len(times)
        complete_times.append(average)


print(complete_times)
"""

results = [[5.9182116985321045, 6.457092049159701, 8.926581612541563, 8.546734298571709, 9.326071683641462,
            8.73551693757375, 9.483254442517719, 8.918806501891877, 8.319338160166664, 9.443650923106405,
            11.718180179595947, 23.660734042478254, 22.850718148945305, 21.90590190083116, 21.62157201834094,
            20.37886680996779, 20.18457189217641, 19.081962598567056, 18.147870289108273, 19.14177756496213,
            10.954182386398315, 24.879614923338483, 33.67663875666755, 34.17340965688854, 40.10108118751141,
            43.450180334925086, 42.422260633283855, 40.27414969537514, 35.26108898415801, 37.5524808561463,
            28.502620697021484, 47.25497700448208, 50.60586695518306, 47.78921402837075, 52.45828945312907,
            50.47762816381589, 52.39336645960359, 52.014317184041225, 52.9792944401958, 50.41190805939457,
            43.075464963912964, 76.65857781168111, 66.22740946320852, 63.96825452642088, 64.51781797459249,
            65.94336670203903, 64.52024221885668, 64.45978976820716, 64.43234227817725, 67.00908848692352],
           [5.9182116985321045, 6.457092049159701, 8.926581612541563, 8.546734298571709, 9.326071683641462,
            8.73551693757375, 9.483254442517719, 8.918806501891877, 8.319338160166664, 9.443650923106405,
            11.718180179595947, 23.660734042478254, 22.850718148945305, 21.90590190083116, 21.62157201834094,
            20.37886680996779, 20.18457189217641, 19.081962598567056, 18.147870289108273, 19.14177756496213,
            10.954182386398315, 24.879614923338483, 33.67663875666755, 34.17340965688854, 40.10108118751141,
            43.450180334925086, 42.422260633283855, 40.27414969537514, 35.26108898415801, 37.5524808561463,
            28.502620697021484, 47.25497700448208, 50.60586695518306, 47.78921402837075, 52.45828945312907,
            50.47762816381589, 52.39336645960359, 52.014317184041225, 52.9792944401958, 50.41190805939457,
            43.075464963912964, 76.65857781168111, 66.22740946320852, 63.96825452642088, 64.51781797459249,
            65.94336670203903, 64.52024221885668, 64.45978976820716, 64.43234227817725, 67.00908848692352],
           [5.9182116985321045, 6.457092049159701, 8.926581612541563, 8.546734298571709, 9.326071683641462,
            8.73551693757375, 9.483254442517719, 8.918806501891877, 8.319338160166664, 9.443650923106405,
            11.718180179595947, 23.660734042478254, 22.850718148945305, 21.90590190083116, 21.62157201834094,
            20.37886680996779, 20.18457189217641, 19.081962598567056, 18.147870289108273, 19.14177756496213,
            10.954182386398315, 24.879614923338483, 33.67663875666755, 34.17340965688854, 40.10108118751141,
            43.450180334925086, 42.422260633283855, 40.27414969537514, 35.26108898415801, 37.5524808561463,
            28.502620697021484, 47.25497700448208, 50.60586695518306, 47.78921402837075, 52.45828945312907,
            50.47762816381589, 52.39336645960359, 52.014317184041225, 52.9792944401958, 50.41190805939457,
            43.075464963912964, 76.65857781168111, 66.22740946320852, 63.96825452642088, 64.51781797459249,
            65.94336670203903, 64.52024221885668, 64.45978976820716, 64.43234227817725, 67.00908848692352],
           [5.9182116985321045, 6.457092049159701, 8.926581612541563, 8.546734298571709, 9.326071683641462,
            8.73551693757375, 9.483254442517719, 8.918806501891877, 8.319338160166664, 9.443650923106405,
            11.718180179595947, 23.660734042478254, 22.850718148945305, 21.90590190083116, 21.62157201834094,
            20.37886680996779, 20.18457189217641, 19.081962598567056, 18.147870289108273, 19.14177756496213,
            10.954182386398315, 24.879614923338483, 33.67663875666755, 34.17340965688854, 40.10108118751141,
            43.450180334925086, 42.422260633283855, 40.27414969537514, 35.26108898415801, 37.5524808561463,
            28.502620697021484, 47.25497700448208, 50.60586695518306, 47.78921402837075, 52.45828945312907,
            50.47762816381589, 52.39336645960359, 52.014317184041225, 52.9792944401958, 50.41190805939457,
            43.075464963912964, 76.65857781168111, 66.22740946320852, 63.96825452642088, 64.51781797459249,
            65.94336670203903, 64.52024221885668, 64.45978976820716, 64.43234227817725, 67.00908848692352],
           [5.9182116985321045, 6.457092049159701, 8.926581612541563, 8.546734298571709, 9.326071683641462,
            8.73551693757375, 9.483254442517719, 8.918806501891877, 8.319338160166664, 9.443650923106405,
            11.718180179595947, 23.660734042478254, 22.850718148945305, 21.90590190083116, 21.62157201834094,
            20.37886680996779, 20.18457189217641, 19.081962598567056, 18.147870289108273, 19.14177756496213,
            10.954182386398315, 24.879614923338483, 33.67663875666755, 34.17340965688854, 40.10108118751141,
            43.450180334925086, 42.422260633283855, 40.27414969537514, 35.26108898415801, 37.5524808561463,
            28.502620697021484, 47.25497700448208, 50.60586695518306, 47.78921402837075, 52.45828945312907,
            50.47762816381589, 52.39336645960359, 52.014317184041225, 52.9792944401958, 50.41190805939457,
            43.075464963912964, 76.65857781168111, 66.22740946320852, 63.96825452642088, 64.51781797459249,
            65.94336670203903, 64.52024221885668, 64.45978976820716, 64.43234227817725, 67.00908848692352]]

x = [10, 20, 30, 40, 50]
y = [8.407525830770295, 14.138370687633813, 20.85041670557897, 27.759999590315164, 35.02424675613252]
width = 5
plt.bar(x, y, width)
plt.title("Cost of set up")
plt.ylabel("Seconds")
plt.xlabel("Number of devices")
plt.gca()
plt.show()
