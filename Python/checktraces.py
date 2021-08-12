'''
A Python script to check if the data conversion (mseed <--> EFS) is OK
usage: python checktraces.py
'''

import os
import numpy as np
import obspy
from EFSpy_module import EFS
import matplotlib.pyplot as plt

def main():

    # load EFS file
    efsname = '../EX_DATA/EFS_Example.efs'
    efs_data = EFS(efsname)

    # load original mseed files
    miniSEED = '../EX_DATA/CI/waveforms/*'
    st = obspy.read(miniSEED)

    # check if the data conversion between mseed and EFS is OK
    j = np.random.randint(0,len(st)) # random station ID
    mseedTrace = st[j].copy()
    wf = efs_data.waveforms[j]

    # display station code, location, and channel
    print('EFS  :', efs_data.waveforms[j]['stname'].strip(), efs_data.waveforms[j]['loccode'].strip(), efs_data.waveforms[j]['chnm'].strip())
    print('mseed:', st[j].stats.station, st[j].stats.location, st[j].stats.channel)

    # judge if the two traces are identical
    if (wf['data'] == mseedTrace.data).all():
        print('two traces are identical!')
    else:
        print('something wrong...')

    # plot traces
    fig, (ax1, ax2) = plt.subplots(2, 1)

    ax1.plot(wf['data'], lw=0.75, color='k', label='EFS: '+st[j].stats.station+' station')
    ax1.plot(mseedTrace.data, lw=0.75, linestyle='-', color='r', label='mseed: '+efs_data.waveforms[j]['stname'].strip()+' station')
    ax1.legend()

    ax2.plot(wf['data'] - mseedTrace.data, color='C7', label='diff')
    ax2.legend()
    plt.show()

if __name__ == '__main__':
    main()
