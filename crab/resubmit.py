import os,sys

crabdir = "/data9/Users/youngwan/work/HNTypeI_TnP/CMSSW_10_6_13/src/EgammaAnalysis/TnPTreeProducer/crab/crab_ElectronTnP_HNTypeI_UL"
dirs = [ name for name in os.listdir(crabdir) if os.path.isdir(os.path.join(crabdir, name)) and "UL" in name ]
for d in dirs :
  os.system(f"crab resubmit -d crab_ElectronTnP_HNTypeI_UL/{d}")
