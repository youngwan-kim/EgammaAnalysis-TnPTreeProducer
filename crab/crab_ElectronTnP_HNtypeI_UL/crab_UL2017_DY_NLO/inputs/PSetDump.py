import FWCore.ParameterSet.Config as cms

process = cms.Process("tnpEGM")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:/eos/cms/store/group/phys_egamma/tnpTuples/testFiles/RunIISummer19UL17MiniAOD-DYJetsToLL_M-50.root')
)
process.HFRecalParameterBlock = cms.PSet(
    HFdepthOneParameterA = cms.vdouble(
        0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
        0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
        0.058939, 0.125497
    ),
    HFdepthOneParameterB = cms.vdouble(
        -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
        2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
        0.000425, 0.000209
    ),
    HFdepthTwoParameterA = cms.vdouble(
        0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
        0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
        0.051579, 0.086593
    ),
    HFdepthTwoParameterB = cms.vdouble(
        -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
        1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
        0.000157, -3e-06
    )
)

process.combinedSecondaryVertexCommon = cms.PSet(
    SoftLeptonFlip = cms.bool(False),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)

process.ghostTrackCommon = cms.PSet(
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig')
)

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.mvaEleID_Fall17_iso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_iso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17IsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
    )
)

process.mvaEleID_Fall17_noIso_V2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Fall17NoIsoV2'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_GeneralPurpose_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) < 0.800', 
        'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16GeneralPurposeV1'),
    nCategories = cms.int32(3),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
    )
)

process.mvaEleID_Spring16_HZZ_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'pt < 10. && abs(superCluster.eta) < 0.800', 
        'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt < 10. && abs(superCluster.eta) >= 1.479', 
        'pt >= 10. && abs(superCluster.eta) < 0.800', 
        'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
        'pt >= 10. && abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('ElectronMVAEstimatorRun2'),
    mvaTag = cms.string('Spring16HZZV1'),
    nCategories = cms.int32(6),
    variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
        'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v1p1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v1p1'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v1p1_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.67, 0.54),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp80'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v1p1_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Categories"),
        mvaCuts = cms.vdouble(0.27, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v1p1-wp90'),
    isPOGApproved = cms.untracked.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('RunIIFall17v2'),
    nCategories = cms.int32(2),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
    )
)

process.mvaPhoID_RunIIFall17_v2_wp80 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(0.42, 0.14),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_RunIIFall17_v2_wp90 = cms.PSet(
    cutFlow = cms.VPSet(cms.PSet(
        cutName = cms.string('PhoMVACut'),
        isIgnored = cms.bool(False),
        mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
        mvaCuts = cms.vdouble(-0.02, -0.26),
        mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        needsAdditionalProducts = cms.bool(True)
    )),
    idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
    isPOGApproved = cms.bool(True)
)

process.mvaPhoID_Spring16_nonTrig_V1_producer_config = cms.PSet(
    categoryCuts = cms.vstring(
        'abs(superCluster.eta) <  1.479', 
        'abs(superCluster.eta) >= 1.479'
    ),
    effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
    mvaName = cms.string('PhotonMVAEstimator'),
    mvaTag = cms.string('Run2Spring16NonTrigV1'),
    nCategories = cms.int32(2),
    phoIsoCutoff = cms.double(2.5),
    phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
    variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
    weightFileNames = cms.vstring(
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
        'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
    )
)

process.options = cms.untracked.PSet(
    wantSummary = cms.untracked.bool(True)
)

process.softPFElectronCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)

process.softPFMuonCommon = cms.PSet(
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)

process.trackPseudoSelectionBlock = cms.PSet(
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.trackSelectionBlock = cms.PSet(
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    )
)

process.variableJTAPars = cms.PSet(
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5)
)

process.c_vs_b_vars_vpset = cms.VPSet(
    cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSig_0'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip2dSig_1'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPPar_0'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPPar_1'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(0),
        name = cms.string('trackPParRatio_0'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(1),
        name = cms.string('trackPParRatio_1'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('jetNTracks'),
        taggingVarName = cms.string('jetNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexMass_0'),
        taggingVarName = cms.string('vertexMass')
    ), 
    cms.PSet(
        default = cms.double(-10),
        idx = cms.int32(0),
        name = cms.string('vertexEnergyRatio_0'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip2dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance2dSig_0'),
        taggingVarName = cms.string('flightDistance2dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance3dSig_0'),
        taggingVarName = cms.string('flightDistance3dSig')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexJetDeltaR_0'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(0),
        idx = cms.int32(0),
        name = cms.string('vertexNTracks_0'),
        taggingVarName = cms.string('vertexNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('massVertexEnergyFraction_0'),
        taggingVarName = cms.string('massVertexEnergyFraction')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexBoostOverSqrtJetPt_0'),
        taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonPtRel_0'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonPtRel_1'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(0),
        name = cms.string('leptonSip3d_0'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(1),
        name = cms.string('leptonSip3d_1'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonDeltaR_0'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonDeltaR_1'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatioRel_0'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatioRel_1'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonEtaRel_0'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonEtaRel_1'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatio_0'),
        taggingVarName = cms.string('leptonRatio')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatio_1'),
        taggingVarName = cms.string('leptonRatio')
    )
)

process.c_vs_l_vars_vpset = cms.VPSet(
    cms.PSet(
        default = cms.double(-1),
        name = cms.string('vertexLeptonCategory'),
        taggingVarName = cms.string('vertexLeptonCategory')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSig_0'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip2dSig_1'),
        taggingVarName = cms.string('trackSip2dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSig_0'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-100),
        idx = cms.int32(1),
        name = cms.string('trackSip3dSig_1'),
        taggingVarName = cms.string('trackSip3dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPtRel_0'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPtRel_1'),
        taggingVarName = cms.string('trackPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackPPar_0'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackPPar_1'),
        taggingVarName = cms.string('trackPPar')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('trackEtaRel_0'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('trackEtaRel_1'),
        taggingVarName = cms.string('trackEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDeltaR_0'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDeltaR_1'),
        taggingVarName = cms.string('trackDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackPtRatio_0'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackPtRatio_1'),
        taggingVarName = cms.string('trackPtRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(0),
        name = cms.string('trackPParRatio_0'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(1.1),
        idx = cms.int32(1),
        name = cms.string('trackPParRatio_1'),
        taggingVarName = cms.string('trackPParRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackJetDist_0'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackJetDist_1'),
        taggingVarName = cms.string('trackJetDist')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('trackDecayLenVal_0'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(1),
        name = cms.string('trackDecayLenVal_1'),
        taggingVarName = cms.string('trackDecayLenVal')
    ), 
    cms.PSet(
        default = cms.double(0),
        name = cms.string('jetNSecondaryVertices'),
        taggingVarName = cms.string('jetNSecondaryVertices')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('jetNTracks'),
        taggingVarName = cms.string('jetNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetEtRatio'),
        taggingVarName = cms.string('trackSumJetEtRatio')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        name = cms.string('trackSumJetDeltaR'),
        taggingVarName = cms.string('trackSumJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexMass_0'),
        taggingVarName = cms.string('vertexMass')
    ), 
    cms.PSet(
        default = cms.double(-10),
        idx = cms.int32(0),
        name = cms.string('vertexEnergyRatio_0'),
        taggingVarName = cms.string('vertexEnergyRatio')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip2dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip2dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-999),
        idx = cms.int32(0),
        name = cms.string('trackSip3dSigAboveCharm_0'),
        taggingVarName = cms.string('trackSip3dSigAboveCharm')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance2dSig_0'),
        taggingVarName = cms.string('flightDistance2dSig')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('flightDistance3dSig_0'),
        taggingVarName = cms.string('flightDistance3dSig')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexJetDeltaR_0'),
        taggingVarName = cms.string('vertexJetDeltaR')
    ), 
    cms.PSet(
        default = cms.double(0),
        idx = cms.int32(0),
        name = cms.string('vertexNTracks_0'),
        taggingVarName = cms.string('vertexNTracks')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('massVertexEnergyFraction_0'),
        taggingVarName = cms.string('massVertexEnergyFraction')
    ), 
    cms.PSet(
        default = cms.double(-0.1),
        idx = cms.int32(0),
        name = cms.string('vertexBoostOverSqrtJetPt_0'),
        taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonPtRel_0'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonPtRel_1'),
        taggingVarName = cms.string('leptonPtRel')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(0),
        name = cms.string('leptonSip3d_0'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-10000),
        idx = cms.int32(1),
        name = cms.string('leptonSip3d_1'),
        taggingVarName = cms.string('leptonSip3d')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonDeltaR_0'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonDeltaR_1'),
        taggingVarName = cms.string('leptonDeltaR')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatioRel_0'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatioRel_1'),
        taggingVarName = cms.string('leptonRatioRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonEtaRel_0'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonEtaRel_1'),
        taggingVarName = cms.string('leptonEtaRel')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(0),
        name = cms.string('leptonRatio_0'),
        taggingVarName = cms.string('leptonRatio')
    ), 
    cms.PSet(
        default = cms.double(-1),
        idx = cms.int32(1),
        name = cms.string('leptonRatio_1'),
        taggingVarName = cms.string('leptonRatio')
    )
)

process.mvaConfigsForEleProducer = cms.VPSet(
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16HZZV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) < 0.800', 
            'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Spring16GeneralPurposeV1'),
        nCategories = cms.int32(3),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV1'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17NoIsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'pt < 10. && abs(superCluster.eta) < 0.800', 
            'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt < 10. && abs(superCluster.eta) >= 1.479', 
            'pt >= 10. && abs(superCluster.eta) < 0.800', 
            'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
            'pt >= 10. && abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('ElectronMVAEstimatorRun2'),
        mvaTag = cms.string('Fall17IsoV2'),
        nCategories = cms.int32(6),
        variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
            'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
        )
    )
)

process.mvaConfigsForPhoProducer = cms.VPSet(
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('Run2Spring16NonTrigV1'),
        nCategories = cms.int32(2),
        phoIsoCutoff = cms.double(2.5),
        phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v1p1'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
        )
    ), 
    cms.PSet(
        categoryCuts = cms.vstring(
            'abs(superCluster.eta) <  1.479', 
            'abs(superCluster.eta) >= 1.479'
        ),
        mvaName = cms.string('PhotonMVAEstimator'),
        mvaTag = cms.string('RunIIFall17v2'),
        nCategories = cms.int32(2),
        variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
        weightFileNames = cms.vstring(
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
            'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
        )
    )
)

process.egmGsfElectronIDs = cms.EDProducer("VersionedGsfElectronIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00477),
                        dEtaInSeedCutValueEE = cms.double(0.00868),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.222),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0314),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.298),
                        hadronicOverEMCutValueEE = cms.double(0.101),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.241),
                        eInverseMinusPInverseCutValueEE = cms.double(0.14),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0994),
                        isoCutEBLowPt = cms.double(0.0994),
                        isoCutEEHighPt = cms.double(0.107),
                        isoCutEELowPt = cms.double(0.107),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c1c4c739f1ba0791d40168c123183475'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00311),
                        dEtaInSeedCutValueEE = cms.double(0.00609),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.103),
                        dPhiInCutValueEE = cms.double(0.045),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0298),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.253),
                        hadronicOverEMCutValueEE = cms.double(0.0878),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.134),
                        eInverseMinusPInverseCutValueEE = cms.double(0.13),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0695),
                        isoCutEBLowPt = cms.double(0.0695),
                        isoCutEEHighPt = cms.double(0.0821),
                        isoCutEELowPt = cms.double(0.0821),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('71b43f74a27d2fd3d27416afd22e8692'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00308),
                        dEtaInSeedCutValueEE = cms.double(0.00605),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0816),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.00998),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0292),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0414),
                        hadronicOverEMCutValueEE = cms.double(0.0641),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0129),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0588),
                        isoCutEBLowPt = cms.double(0.0588),
                        isoCutEEHighPt = cms.double(0.0571),
                        isoCutEELowPt = cms.double(0.0571),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('ca2a9db2976d80ba2c13f9bfccdc32f2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00749),
                        dEtaInSeedCutValueEE = cms.double(0.00895),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.228),
                        dPhiInCutValueEE = cms.double(0.213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0115),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.037),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.356),
                        hadronicOverEMCutValueEE = cms.double(0.211),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.299),
                        eInverseMinusPInverseCutValueEE = cms.double(0.15),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.175),
                        isoCutEBLowPt = cms.double(0.175),
                        isoCutEEHighPt = cms.double(0.159),
                        isoCutEELowPt = cms.double(0.159),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Summer16-80X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0025c1841da1ab64a08d703ded72409b'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(35.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.4442),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.566)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(0.006),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.06),
                        dPhiInCutValueEE = cms.double(0.06),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(9999),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.03),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('GsfEleFull5x5E2x5OverE5x5Cut'),
                        isIgnored = cms.bool(False),
                        minE1x5OverE5x5EB = cms.double(0.83),
                        minE1x5OverE5x5EE = cms.double(-1.0),
                        minE2x5OverE5x5EB = cms.double(0.94),
                        minE2x5OverE5x5EE = cms.double(-1.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.0),
                        constTermEE = cms.double(5),
                        cutName = cms.string('GsfEleHadronicOverEMLinearCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.05),
                        slopeTermEE = cms.double(0.05)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(5.0),
                        constTermEE = cms.double(5.0),
                        cutName = cms.string('GsfEleTrkPtIsoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.0),
                        slopeTermEE = cms.double(0.0),
                        useHEEPIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.0),
                        constTermEE = cms.double(2.5),
                        cutName = cms.string('GsfEleEmHadD1IsoRhoCut'),
                        energyType = cms.string('EcalTrk'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll"),
                        rhoConstant = cms.double(0.28),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(50.0),
                        slopeTermEB = cms.double(0.03),
                        slopeTermEE = cms.double(0.03)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDxyCut'),
                        dxyCutValueEB = cms.double(0.02),
                        dxyCutValueEE = cms.double(0.05),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        vertexSrc = cms.InputTag("offlinePrimaryVertices"),
                        vertexSrcMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEcalDrivenCut'),
                        ecalDrivenEB = cms.int32(1),
                        ecalDrivenEE = cms.int32(1),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('heepElectronID-HEEPV60'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('df10ac7e3a9c22f63fa7936573beaafb'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.940962684155', 
                        '0.899208843708', 
                        '0.758484721184'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('b490bc0b0af2d5f3e9efea562370af2a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.836695742607', 
                        '0.715337944031', 
                        '0.356799721718'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Spring16-GeneralPurpose-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('14c153aaf3c207deb3ad4932586647a7'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00387),
                        dEtaInSeedCutValueEE = cms.double(0.0072),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0716),
                        dPhiInCutValueEE = cms.double(0.147),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0356),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0414),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.129),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0875),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.133),
                        isoCutEBLowPt = cms.double(0.133),
                        isoCutEEHighPt = cms.double(0.146),
                        isoCutEELowPt = cms.double(0.146),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('0b8456d622494441fe713a6858e0f7c1'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00365),
                        dEtaInSeedCutValueEE = cms.double(0.00625),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0588),
                        dPhiInCutValueEE = cms.double(0.0355),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0105),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0309),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0327),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0335),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0718),
                        isoCutEBLowPt = cms.double(0.0718),
                        isoCutEEHighPt = cms.double(0.143),
                        isoCutEELowPt = cms.double(0.143),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('a238ee70910de53d36866e89768500e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00353),
                        dEtaInSeedCutValueEE = cms.double(0.00567),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0499),
                        dPhiInCutValueEE = cms.double(0.0165),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0305),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.026),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.0278),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0158),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.0361),
                        isoCutEBLowPt = cms.double(0.0361),
                        isoCutEEHighPt = cms.double(0.094),
                        isoCutEELowPt = cms.double(0.094),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4acb2d2796efde7fba75380ce8823fc2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00523),
                        dEtaInSeedCutValueEE = cms.double(0.00984),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.159),
                        dPhiInCutValueEE = cms.double(0.157),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0128),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0445),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.12),
                        barrelCr = cms.double(0.0368),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(0.5),
                        endcapCr = cms.double(0.201),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0962),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEffAreaPFIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_92X.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.168),
                        isoCutEBLowPt = cms.double(0.168),
                        isoCutEEHighPt = cms.double(0.185),
                        isoCutEELowPt = cms.double(0.185),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V1-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('43be9b381a8d9b0910b7f81a5ad8ff3a'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9530240956555949 - exp(-pt / 2.7591425841003647) *  0.4669644718545271', 
                        '0.9336564763961019 - exp(-pt /  2.709276284272272) * 0.33512286599215946', 
                        '0.9313133688365339 - exp(-pt / 1.5821934800715558) *  3.8889462619659265', 
                        '0.9825268564943458 - exp(-pt /  8.702601455860762) *  1.1974861596609097', 
                        '0.9727509457929913 - exp(-pt /  8.179525631018565) *  1.7111755094657688', 
                        '0.9562619539540145 - exp(-pt /  8.109845366281608) *   3.013927699126942'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9165112826974601 - exp(-pt / 2.7381703555094217) *    1.03549199648109', 
                        '0.8655738322220173 - exp(-pt / 2.4027944652597073) *  0.7975615613282494', 
                        '-3016.035055227131 - exp(-pt / -52140.61856333602) * -3016.3029387236506', 
                        '0.9616542816132922 - exp(-pt /  8.757943837889817) *  3.1390200321591206', 
                        '0.9319258011430132 - exp(-pt /  8.846057432565809) *  3.5985063793347787', 
                        '0.8899260780999244 - exp(-pt / 10.124234115859881) *   4.352791250718547'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.13285867293779202', 
                        '-0.31765300958836074', 
                        '-0.0799205914718861', 
                        '-0.856871961305474', 
                        '-0.8107642141584835', 
                        '-0.7179265933023059'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9725509559754997 - exp(-pt /  2.976593261509491) *  0.2653858736397496', 
                        '0.9508038141601247 - exp(-pt / 2.6633500558725713) *  0.2355820499260076', 
                        '0.9365037167596238 - exp(-pt / 1.5765442323949856) *   3.067015289215309', 
                        '0.9896562087723659 - exp(-pt / 10.342490511998674) * 0.40204156417414094', 
                        '0.9819232656533827 - exp(-pt /   9.05548836482051) *   0.772674931169389', 
                        '0.9625098201744635 - exp(-pt /   8.42589315557279) *  2.2916152615134173'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '0.9387070396095831 - exp(-pt /   2.6525585228167636) *  0.8222647164151365', 
                        '0.8948802925677235 - exp(-pt /   2.7645670358783523) *  0.4123381218697539', 
                        '-1830.8583661119892 - exp(-pt /   -36578.11055382301) * -1831.2083578116517', 
                        '0.9717674837607253 - exp(-pt /    8.912850985100356) *  1.9712414940437244', 
                        '0.9458745023265976 - exp(-pt /     8.83104420392795) *    2.40849932040698', 
                        '0.8979112012086751 - exp(-pt /    9.814082144168015) *   4.171581694893849'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Categories"),
                    mvaCuts = cms.vstring(
                        '-0.09564086146419018', 
                        '-0.28229916981926795', 
                        '-0.05466682296962322', 
                        '-0.833466688584422', 
                        '-0.7677000247570116', 
                        '-0.6917305995653829'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V1-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '3.26449620468 - exp(-pt / 3.32657149223) * 8.84669783568', 
                        '2.83557838497 - exp(-pt / 2.15150487651) * 11.0978016567', 
                        '2.91994945177 - exp(-pt / 1.69875477522) * 24.024807824', 
                        '7.1336238874 - exp(-pt / 16.5605268797) * 8.22531222391', 
                        '6.18638275782 - exp(-pt / 15.2694634284) * 7.49764565324', 
                        '5.43175865738 - exp(-pt / 15.4290075949) * 7.56899692285'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '2.77072387339 - exp(-pt / 3.81500912145) * 8.16304860178', 
                        '1.85602317813 - exp(-pt / 2.18697654938) * 11.8568936824', 
                        '1.73489307814 - exp(-pt / 2.0163211971) * 17.013880078', 
                        '5.9175992258 - exp(-pt / 13.4807294538) * 9.31966232685', 
                        '5.01598837255 - exp(-pt / 13.1280451502) * 8.79418193765', 
                        '4.16921343208 - exp(-pt / 13.2017224621) * 9.00720913211'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '0.894411158628', 
                        '0.791966464633', 
                        '1.47104857173', 
                        '-0.293962958665', 
                        '-0.250424758584', 
                        '-0.130985179031'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-noIso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '3.53495358797 - exp(-pt / 3.07272325141) * 9.94262764352', 
                        '3.06015605623 - exp(-pt / 1.95572234114) * 14.3091184421', 
                        '3.02052519639 - exp(-pt / 1.59784164742) * 28.719380105', 
                        '7.35752275071 - exp(-pt / 15.87907864) * 7.61288809226', 
                        '6.41811074032 - exp(-pt / 14.730562874) * 6.96387331587', 
                        '5.64936312428 - exp(-pt / 16.3664949747) * 7.19607610311'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '2.84704783417 - exp(-pt / 3.32529515837) * 9.38050947827', 
                        '2.03833922005 - exp(-pt / 1.93288758682) * 15.364588247', 
                        '1.82704158461 - exp(-pt / 1.89796754399) * 19.1236071158', 
                        '6.12931925263 - exp(-pt / 13.281753835) * 8.71138432196', 
                        '5.26289004857 - exp(-pt / 13.2154971491) * 8.0997882835', 
                        '4.37338792902 - exp(-pt / 14.0776094696) * 8.48513324496'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '1.26402092475', 
                        '1.17808089508', 
                        '1.33051972806', 
                        '2.36464785939', 
                        '2.07880614597', 
                        '1.08080644615'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpHZZ'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('GsfEleMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Categories"),
                    mvaCuts = cms.vstring(
                        '0.700642584415', 
                        '0.739335420875', 
                        '1.45390456109', 
                        '-0.146270871164', 
                        '-0.0315850882679', 
                        '-0.0321841194737'
                    ),
                    mvaValueMapName = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaEleID-Fall17-iso-V2-wpLoose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00377),
                        dEtaInSeedCutValueEE = cms.double(0.00674),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0884),
                        dPhiInCutValueEE = cms.double(0.169),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0112),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0425),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0441),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.193),
                        eInverseMinusPInverseCutValueEE = cms.double(0.111),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.112),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.108),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('5547e2c8b5c222192519c41bff05bc2e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.0032),
                        dEtaInSeedCutValueEE = cms.double(0.00632),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.0547),
                        dPhiInCutValueEE = cms.double(0.0394),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0106),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0387),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.046),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0275),
                        endcapCE = cms.double(2.52),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.184),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0721),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0478),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0658),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('48702f025a8df2c527f53927af8b66d0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00255),
                        dEtaInSeedCutValueEE = cms.double(0.00501),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.022),
                        dPhiInCutValueEE = cms.double(0.0236),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0104),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0353),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.026),
                        barrelCE = cms.double(1.15),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.0188),
                        endcapCE = cms.double(2.06),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.159),
                        eInverseMinusPInverseCutValueEE = cms.double(0.0197),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.0287),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.0445),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(1),
                        maxMissingHitsEE = cms.uint32(1),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c06761e199f084f5b0f7868ac48a3e19'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.00463),
                        dEtaInSeedCutValueEE = cms.double(0.00814),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.148),
                        dPhiInCutValueEE = cms.double(0.19),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.0126),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.0457),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.05),
                        barrelCE = cms.double(1.16),
                        barrelCr = cms.double(0.0324),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMEnergyScaledCut'),
                        endcapC0 = cms.double(0.05),
                        endcapCE = cms.double(2.54),
                        endcapCr = cms.double(0.183),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.209),
                        eInverseMinusPInverseCutValueEE = cms.double(0.132),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelC0 = cms.double(0.198),
                        barrelCpt = cms.double(0.506),
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleRelPFIsoScaledCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
                        endcapC0 = cms.double(0.203),
                        endcapCpt = cms.double(0.963),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        beamspotSrc = cms.InputTag("offlineBeamSpot"),
                        conversionSrc = cms.InputTag("allConversions"),
                        conversionSrcMiniAOD = cms.InputTag("reducedEgamma","reducedConversions"),
                        cutName = cms.string('GsfEleConversionVetoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleMissingHitsCut'),
                        isIgnored = cms.bool(False),
                        maxMissingHitsEB = cms.uint32(2),
                        maxMissingHitsEE = cms.uint32(3),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedElectronID-Fall17-94X-V2-veto'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('74e217e3ece16b49bd337026a29fc3e9'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.031),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.004),
                        dEtaInSeedCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.02),
                        dPhiInCutValueEE = cms.double(1e+30),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.06),
                        hadronicOverEMCutValueEE = cms.double(0.065),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.013),
                        eInverseMinusPInverseCutValueEE = cms.double(0.013),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_ecalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.16),
                        isoCutEBLowPt = cms.double(0.16),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(0),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetCentralCalo")
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleCalPFClusterIsoCut'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_HLT_hcalPFClusterIso.txt'),
                        isIgnored = cms.bool(False),
                        isRelativeIso = cms.bool(True),
                        isoCutEBHighPt = cms.double(0.12),
                        isoCutEBLowPt = cms.double(0.12),
                        isoCutEEHighPt = cms.double(0.12),
                        isoCutEELowPt = cms.double(0.12),
                        isoType = cms.int32(1),
                        needsAdditionalProducts = cms.bool(True),
                        ptCutOff = cms.double(20.0),
                        rho = cms.InputTag("fixedGridRhoFastjetCentralCalo")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.0),
                        constTermEE = cms.double(0.0),
                        cutName = cms.string('GsfEleTrkPtIsoCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        slopeStartEB = cms.double(0.0),
                        slopeStartEE = cms.double(0.0),
                        slopeTermEB = cms.double(0.08),
                        slopeTermEE = cms.double(0.08),
                        useHEEPIso = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleNormalizedGsfChi2Cut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        normalizedGsfChi2CutValueEB = cms.double(1e+30),
                        normalizedGsfChi2CutValueEE = cms.double(3.0)
                    )
                ),
                idName = cms.string('cutBasedElectronHLTPreselection-Summer16-V1'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('aef5f00cc25a63b44192c6fc449f7dc0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('GsfEleSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleFull5x5SigmaIEtaIEtaCut'),
                        full5x5SigmaIEtaIEtaCutValueEB = cms.double(0.011),
                        full5x5SigmaIEtaIEtaCutValueEE = cms.double(0.031),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDEtaInSeedCut'),
                        dEtaInSeedCutValueEB = cms.double(0.01),
                        dEtaInSeedCutValueEE = cms.double(0.01),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleDPhiInCut'),
                        dPhiInCutValueEB = cms.double(0.04),
                        dPhiInCutValueEE = cms.double(0.08),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleHadronicOverEMCut'),
                        hadronicOverEMCutValueEB = cms.double(0.08),
                        hadronicOverEMCutValueEE = cms.double(0.08),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('GsfEleEInverseMinusPInverseCut'),
                        eInverseMinusPInverseCutValueEB = cms.double(0.01),
                        eInverseMinusPInverseCutValueEE = cms.double(0.01),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('PatEleEBEECut'),
                        cutString = cms.string('ecalPFClusterIso/pt'),
                        cutValueEB = cms.double(0.45),
                        cutValueEE = cms.double(0.45),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('PatEleEBEECut'),
                        cutString = cms.string('hcalPFClusterIso/pt'),
                        cutValueEB = cms.double(0.25),
                        cutValueEE = cms.double(0.25),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        cutName = cms.string('PatEleEBEECut'),
                        cutString = cms.string('dr03TkSumPt/pt'),
                        cutValueEB = cms.double(0.2),
                        cutValueEE = cms.double(0.2),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    )
                ),
                idName = cms.string('cutBasedDoubleElectronHLTPreselection-Summer16-V1'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string(''),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("slimmedElectrons")
)


process.egmPhotonIDs = cms.EDProducer("VersionedPhotonIdProducer",
    physicsObjectIDs = cms.VPSet(
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0597),
                        hadronicOverEMCutValueEE = cms.double(0.0481),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01031),
                        cutValueEE = cms.double(0.03013),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.295),
                        constTermEE = cms.double(1.011),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(10.91),
                        constTermEE = cms.double(5.931),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0148),
                        linearPtTermEE = cms.double(0.0163),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(1.7e-05),
                        quadPtTermEE = cms.double(1.4e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(3.63),
                        constTermEE = cms.double(6.641),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0047),
                        linearPtTermEE = cms.double(0.0034),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('d6ce6a4f3476294bf0a3261e00170daf'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0396),
                        hadronicOverEMCutValueEE = cms.double(0.0219),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01022),
                        cutValueEE = cms.double(0.03001),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.441),
                        constTermEE = cms.double(0.442),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.725),
                        constTermEE = cms.double(1.715),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0148),
                        linearPtTermEE = cms.double(0.0163),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(1.7e-05),
                        quadPtTermEE = cms.double(1.4e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.571),
                        constTermEE = cms.double(3.863),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0047),
                        linearPtTermEE = cms.double(0.0034),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('c739cfd0b6287b8586da187c06d4053f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.0269),
                        hadronicOverEMCutValueEE = cms.double(0.0213),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00994),
                        cutValueEE = cms.double(0.03),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.202),
                        constTermEE = cms.double(0.034),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.264),
                        constTermEE = cms.double(0.586),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0148),
                        linearPtTermEE = cms.double(0.0163),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(1.7e-05),
                        quadPtTermEE = cms.double(1.4e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.362),
                        constTermEE = cms.double(2.617),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0047),
                        linearPtTermEE = cms.double(0.0034),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Spring16-V2p2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('bdb623bdb1a15c13545020a919dd9530'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.68, 0.6),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp80'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('beb95233f7d1e033ad9e20cf3d804ba0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Categories"),
                    mvaCuts = cms.vdouble(0.2, 0.2),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-Spring16-nonTrig-V1-wp90'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('36efe663348f95de0bc1cfa8dc7fa8fe'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.043),
                        hadronicOverEMCutValueEE = cms.double(0.026),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0101),
                        cutValueEE = cms.double(0.0267),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.403),
                        constTermEE = cms.double(2.809),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(15.959),
                        constTermEE = cms.double(7.056),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0127),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.6e-05),
                        quadPtTermEE = cms.double(2.5e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(3.06),
                        constTermEE = cms.double(4.766),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0038),
                        linearPtTermEE = cms.double(0.0038),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('08547098f52eb608b545953f02583c3f'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.032),
                        hadronicOverEMCutValueEE = cms.double(0.0219),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0101),
                        cutValueEE = cms.double(0.03001),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.43),
                        constTermEE = cms.double(0.442),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.133),
                        constTermEE = cms.double(1.715),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0127),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.6e-05),
                        quadPtTermEE = cms.double(2.5e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.344),
                        constTermEE = cms.double(3.863),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0038),
                        linearPtTermEE = cms.double(0.0038),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('fb58ccd713d6be1f86f1d2e48c69e401'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.022),
                        hadronicOverEMCutValueEE = cms.double(0.021),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0099),
                        cutValueEE = cms.double(0.0267),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.101),
                        constTermEE = cms.double(0.134),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.137),
                        constTermEE = cms.double(1.615),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0127),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.6e-05),
                        quadPtTermEE = cms.double(2.5e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.308),
                        constTermEE = cms.double(3.107),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0038),
                        linearPtTermEE = cms.double(0.0038),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V1-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('296da1cdbf6f35a99287c5a527472ed3'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(0.42, 0.14),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp80'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('3013ddce7a3ad8b54827c29f5d92282e'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(cms.PSet(
                    cutName = cms.string('PhoMVACut'),
                    isIgnored = cms.bool(False),
                    mvaCategoriesMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Categories"),
                    mvaCuts = cms.vdouble(-0.02, -0.26),
                    mvaValueMapName = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
                    needsAdditionalProducts = cms.bool(True)
                )),
                idName = cms.string('mvaPhoID-RunIIFall17-v2-wp90'),
                isPOGApproved = cms.bool(True)
            ),
            idMD5 = cms.string('5c06832759b1faf7dd6fc45ed1aef3a2'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.04596),
                        hadronicOverEMCutValueEE = cms.double(0.059),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.0106),
                        cutValueEE = cms.double(0.0272),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.694),
                        constTermEE = cms.double(2.089),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(24.032),
                        constTermEE = cms.double(19.722),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.01512),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.259e-05),
                        quadPtTermEE = cms.double(2.3e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.876),
                        constTermEE = cms.double(4.162),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.004017),
                        linearPtTermEE = cms.double(0.0037),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-loose'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('4578dfcceb0bfd1ba5ac28973c843fd0'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02197),
                        hadronicOverEMCutValueEE = cms.double(0.0326),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.01015),
                        cutValueEE = cms.double(0.0272),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.141),
                        constTermEE = cms.double(1.051),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(1.189),
                        constTermEE = cms.double(2.718),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.01512),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.259e-05),
                        quadPtTermEE = cms.double(2.3e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.08),
                        constTermEE = cms.double(3.867),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.004017),
                        linearPtTermEE = cms.double(0.0037),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-medium'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('28b186c301061395f394a81266c8d7de'),
            isPOGApproved = cms.untracked.bool(True)
        ), 
        cms.PSet(
            idDefinition = cms.PSet(
                cutFlow = cms.VPSet(
                    cms.PSet(
                        cutName = cms.string('MinPtCut'),
                        isIgnored = cms.bool(False),
                        minPt = cms.double(5.0),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        allowedEtaRanges = cms.VPSet(
                            cms.PSet(
                                maxEta = cms.double(1.479),
                                minEta = cms.double(0.0)
                            ), 
                            cms.PSet(
                                maxEta = cms.double(2.5),
                                minEta = cms.double(1.479)
                            )
                        ),
                        cutName = cms.string('PhoSCEtaMultiRangeCut'),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False),
                        useAbsEta = cms.bool(True)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoSingleTowerHadOverEmCut'),
                        hadronicOverEMCutValueEB = cms.double(0.02148),
                        hadronicOverEMCutValueEE = cms.double(0.0321),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        barrelCutOff = cms.double(1.479),
                        cutName = cms.string('PhoFull5x5SigmaIEtaIEtaCut'),
                        cutValueEB = cms.double(0.00996),
                        cutValueEE = cms.double(0.0271),
                        isIgnored = cms.bool(False),
                        needsAdditionalProducts = cms.bool(False)
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.65),
                        constTermEE = cms.double(0.517),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('chargedHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfChargedHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.0),
                        linearPtTermEE = cms.double(0.0),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(0.317),
                        constTermEE = cms.double(2.716),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('neutralHadronIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfNeutralHadrons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.01512),
                        linearPtTermEE = cms.double(0.0117),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(2.259e-05),
                        quadPtTermEE = cms.double(2.3e-05),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    ), 
                    cms.PSet(
                        constTermEB = cms.double(2.044),
                        constTermEE = cms.double(3.032),
                        cutName = cms.string('PhoGenericRhoPtScaledCut'),
                        cutVariable = cms.string('photonIso'),
                        effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Fall17/effAreaPhotons_cone03_pfPhotons_90percentBased_V2.txt'),
                        isIgnored = cms.bool(False),
                        lessThan = cms.bool(True),
                        linearPtTermEB = cms.double(0.004017),
                        linearPtTermEE = cms.double(0.0037),
                        needsAdditionalProducts = cms.bool(True),
                        quadPtTermEB = cms.double(0.0),
                        quadPtTermEE = cms.double(0.0),
                        rho = cms.InputTag("fixedGridRhoFastjetAll")
                    )
                ),
                idName = cms.string('cutBasedPhotonID-Fall17-94X-V2-tight'),
                isPOGApproved = cms.untracked.bool(True)
            ),
            idMD5 = cms.string('6f4f0ed6a8bf2de8dcf0bc3349b0546d'),
            isPOGApproved = cms.untracked.bool(True)
        )
    ),
    physicsObjectSrc = cms.InputTag("slimmedPhotons")
)


process.eleVarHelper = cms.EDProducer("PatElectronVariableHelper",
    beamSpot = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("reducedEgamma","reducedConversions"),
    l1EGColl = cms.InputTag("caloStage2Digis","EGamma"),
    pfCandidates = cms.InputTag("packedPFCandidates"),
    probes = cms.InputTag("slimmedElectrons"),
    rhoLabel = cms.InputTag("fixedGridRhoFastjetAll"),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.electronMVAValueMapProducer = cms.EDProducer("ElectronMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16HZZV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_HZZ_V1/electronID_mva_Spring16_HZZ_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) < 0.800', 
                'abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Spring16GeneralPurposeV1'),
            nCategories = cms.int32(3),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Spring16_GeneralPurpose_V1/electronID_mva_Spring16_GeneralPurpose_V1_EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV1'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Fall17V1Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_5_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB1_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EB2_10_2017_puinfo_iso_BDT.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/Fall17/EIDmva_EE_10_2017_puinfo_iso_BDT.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17NoIsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17NoIsoV2/EE_10.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'pt < 10. && abs(superCluster.eta) < 0.800', 
                'pt < 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt < 10. && abs(superCluster.eta) >= 1.479', 
                'pt >= 10. && abs(superCluster.eta) < 0.800', 
                'pt >= 10. && abs(superCluster.eta) >= 0.800 && abs(superCluster.eta) < 1.479', 
                'pt >= 10. && abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('ElectronMVAEstimatorRun2'),
            mvaTag = cms.string('Fall17IsoV2'),
            nCategories = cms.int32(6),
            variableDefinition = cms.string('RecoEgamma/ElectronIdentification/data/ElectronMVAEstimatorRun2Variables.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_5.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB1_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EB2_10.weights.xml.gz', 
                'RecoEgamma/ElectronIdentification/data/MVAWeightFiles/Fall17IsoV2/EE_10.weights.xml.gz'
            )
        )
    ),
    src = cms.InputTag("slimmedElectrons"),
    srcMiniAOD = cms.InputTag("slimmedElectrons","","@skipCurrentProcess")
)


process.genProbeEle = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genEle"),
    maxDPtRel = cms.double(50.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("probeEle")
)


process.genProbePho = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genEle"),
    maxDPtRel = cms.double(50.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("probePho")
)


process.genProbeSC = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genEle"),
    maxDPtRel = cms.double(50.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("probeSC")
)


process.genTagEle = cms.EDProducer("MCMatcher",
    checkCharge = cms.bool(False),
    matched = cms.InputTag("genEle"),
    maxDPtRel = cms.double(50.0),
    maxDeltaR = cms.double(0.2),
    mcPdgId = cms.vint32(),
    mcStatus = cms.vint32(),
    resolveAmbiguities = cms.bool(False),
    resolveByMatchQuality = cms.bool(True),
    src = cms.InputTag("tagEle")
)


process.goodElectronProbesL1 = cms.EDProducer("PatElectronL1Stage2CandProducer",
    dRmatch = cms.double(0.2),
    dRmatchEE = cms.double(0.2),
    inputs = cms.InputTag("goodElectrons"),
    isolatedOnly = cms.bool(False),
    minET = cms.double(0),
    objects = cms.InputTag("caloStage2Digis","EGamma")
)


process.isoForEleFall17 = cms.EDProducer("EleIsoValueMapProducer",
    EAFile_MiniIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    EAFile_PFIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Fall17/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_94X.txt'),
    relative = cms.bool(True),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    rho_PFIso = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectrons")
)


process.isoForEleSpring15 = cms.EDProducer("EleIsoValueMapProducer",
    EAFile_MiniIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
    EAFile_PFIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Spring15/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_25ns.txt'),
    relative = cms.bool(True),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    rho_PFIso = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectrons")
)


process.isoForEleSummer16 = cms.EDProducer("EleIsoValueMapProducer",
    EAFile_MiniIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
    EAFile_PFIso = cms.FileInPath('RecoEgamma/ElectronIdentification/data/Summer16/effAreaElectrons_cone03_pfNeuHadronsAndPhotons_80X.txt'),
    relative = cms.bool(True),
    rho_MiniIso = cms.InputTag("fixedGridRhoFastjetAll"),
    rho_PFIso = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedElectrons")
)


process.leptonMvaGhent = cms.EDProducer("LeptonMvaProducer",
    PFIsoAll = cms.InputTag("isoForEleFall17","PFIsoAll"),
    closestJet = cms.InputTag("ptRatioRelForEle","jetForLepJetVar"),
    debug = cms.bool(False),
    jetNDauChargedMVASel = cms.InputTag("ptRatioRelForEle","jetNDauChargedMVASel"),
    leptonMvaType = cms.string('leptonMvaGhent'),
    miniIsoAll = cms.InputTag("isoForEleFall17","miniIsoAll"),
    miniIsoChg = cms.InputTag("isoForEleFall17","miniIsoChg"),
    mvas = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
    probes = cms.InputTag("slimmedElectrons"),
    ptRatio = cms.InputTag("ptRatioRelForEle","ptRatio"),
    ptRel = cms.InputTag("ptRatioRelForEle","ptRel"),
    weightFile = cms.FileInPath('EgammaAnalysis/TnPTreeProducer/data/el_tZqTTV17_BDTG.weights.xml')
)


process.leptonMvaTOP = cms.EDProducer("LeptonMvaProducer",
    PFIsoAll = cms.InputTag("isoForEleFall17","PFIsoAll"),
    closestJet = cms.InputTag("ptRatioRelForEle","jetForLepJetVar"),
    debug = cms.bool(False),
    jetNDauChargedMVASel = cms.InputTag("ptRatioRelForEle","jetNDauChargedMVASel"),
    leptonMvaType = cms.string('leptonMvaTOP'),
    miniIsoAll = cms.InputTag("isoForEleFall17","miniIsoAll"),
    miniIsoChg = cms.InputTag("isoForEleFall17","miniIsoChg"),
    mvas = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
    probes = cms.InputTag("slimmedElectrons"),
    ptRatio = cms.InputTag("ptRatioRelForEle","ptRatio"),
    ptRel = cms.InputTag("ptRatioRelForEle","ptRel"),
    weightFile = cms.FileInPath('EgammaAnalysis/TnPTreeProducer/data/el_TOP17_BDTG.weights.xml')
)


process.leptonMvaTTH = cms.EDProducer("LeptonMvaProducer",
    closestJet = cms.InputTag("ptRatioRelForEle","jetForLepJetVar"),
    debug = cms.bool(False),
    jetNDauChargedMVASel = cms.InputTag("ptRatioRelForEle","jetNDauChargedMVASel"),
    leptonMvaType = cms.string('leptonMvaTTH'),
    miniIsoAll = cms.InputTag("isoForEleFall17","miniIsoAll"),
    miniIsoChg = cms.InputTag("isoForEleFall17","miniIsoChg"),
    mvas = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
    probes = cms.InputTag("slimmedElectrons"),
    ptRatio = cms.InputTag("ptRatioRelForEle","ptRatio"),
    ptRel = cms.InputTag("ptRatioRelForEle","ptRel"),
    weightFile = cms.FileInPath('EgammaAnalysis/TnPTreeProducer/data/el_ttH17_BDTG.weights.xml')
)


process.passEGL1SingleEGOr = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltEGL1SingleEGOrFilter'),
    inputs = cms.InputTag("probeEle"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.passHltDoubleEle33CaloIdLMWSeedLegL1match = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltEle33CaloIdLMWPMS2Filter'),
    inputs = cms.InputTag("probeEleL1matched"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.passHltDoubleEle33CaloIdLMWUnsLeg = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltDiEle33CaloIdLMWPMS2UnseededFilter'),
    inputs = cms.InputTag("probeEle"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg1Filter'),
    inputs = cms.InputTag("probeEleL1matched"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltEle23Ele12CaloIdLTrackIdLIsoVLTrackIsoLeg2Filter'),
    inputs = cms.InputTag("probeEle"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.passHltEle32DoubleEGWPTightGsf = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring('hltEle32L1DoubleEGWPTightGsfTrackIsoFilter'),
    inputs = cms.InputTag("probeEle"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.patJetCorrFactorsTransientCorrectedUpdated = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(
        'L1FastJet', 
        'L2Relative', 
        'L3Absolute'
    ),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("updatedPatJetsUpdated"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.patJetCorrFactorsUpdated = cms.EDProducer("JetCorrFactorsProducer",
    emf = cms.bool(False),
    extraJPTOffset = cms.string('L1FastJet'),
    flavorType = cms.string('J'),
    levels = cms.vstring(),
    payload = cms.string('AK4PFchs'),
    primaryVertices = cms.InputTag("offlineSlimmedPrimaryVertices"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    src = cms.InputTag("slimmedJets"),
    useNPV = cms.bool(True),
    useRho = cms.bool(True)
)


process.pfDeepCSVTagInfosUpdated = cms.EDProducer("DeepNNTagInfoProducer",
    computer = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(True),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    svTagInfos = cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosUpdated")
)


process.pfDeepFlavourJetTagsUpdated = cms.EDProducer("DeepFlavourTFJetTagsProducer",
    batch_eval = cms.bool(False),
    flav_table = cms.PSet(
        probb = cms.vuint32(0),
        probbb = cms.vuint32(1),
        probc = cms.vuint32(3),
        probg = cms.vuint32(5),
        problepb = cms.vuint32(2),
        probuds = cms.vuint32(4)
    ),
    graph_path = cms.FileInPath('RecoBTag/Combined/data/DeepFlavourV03_10X_training/constant_graph.pb'),
    input_names = cms.vstring(
        'input_1', 
        'input_2', 
        'input_3', 
        'input_4', 
        'input_5'
    ),
    lp_names = cms.vstring('cpf_input_batchnorm/keras_learning_phase'),
    nThreads = cms.uint32(1),
    output_names = cms.vstring(
        'ID_pred/Softmax', 
        'regression_pred/BiasAdd'
    ),
    singleThreadPool = cms.string('no_threads'),
    src = cms.InputTag("pfDeepFlavourTagInfosUpdated")
)


process.pfDeepFlavourTagInfosUpdated = cms.EDProducer("DeepFlavourTagInfoProducer",
    fallback_puppi_weight = cms.bool(False),
    fallback_vertex_association = cms.bool(False),
    flip = cms.bool(False),
    jet_radius = cms.double(0.4),
    jets = cms.InputTag("updatedPatJetsUpdated"),
    min_candidate_pt = cms.double(0.95),
    puppi_value_map = cms.InputTag("puppi"),
    secondary_vertices = cms.InputTag("slimmedSecondaryVertices"),
    shallow_tag_infos = cms.InputTag("pfDeepCSVTagInfosUpdated"),
    vertex_associator = cms.InputTag("primaryVertexAssociation","original"),
    vertices = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.pfImpactParameterTagInfosUpdated = cms.EDProducer("CandIPProducer",
    candidates = cms.InputTag("packedPFCandidates"),
    computeGhostTrack = cms.bool(True),
    computeProbabilities = cms.bool(True),
    ghostTrackPriorDeltaR = cms.double(0.03),
    jetDirectionUsingGhostTrack = cms.bool(False),
    jetDirectionUsingTracks = cms.bool(False),
    jets = cms.InputTag("updatedPatJetsUpdated"),
    maxDeltaR = cms.double(0.4),
    maximumChiSquared = cms.double(5.0),
    maximumLongitudinalImpactParameter = cms.double(17.0),
    maximumTransverseImpactParameter = cms.double(0.2),
    minimumNumberOfHits = cms.int32(0),
    minimumNumberOfPixelHits = cms.int32(1),
    minimumTransverseMomentum = cms.double(1.0),
    primaryVertex = cms.InputTag("offlineSlimmedPrimaryVertices"),
    useTrackQuality = cms.bool(False)
)


process.pfInclusiveSecondaryVertexFinderTagInfosUpdated = cms.EDProducer("CandSecondaryVertexProducer",
    beamSpotTag = cms.InputTag("offlineBeamSpot"),
    constraint = cms.string('BeamSpot'),
    extSVCollection = cms.InputTag("slimmedSecondaryVertices"),
    extSVDeltaRToJet = cms.double(0.3),
    minimumTrackWeight = cms.double(0.5),
    trackIPTagInfos = cms.InputTag("pfImpactParameterTagInfosUpdated"),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(99999.9),
        maxDistToAxis = cms.double(0.2),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(1),
        ptMin = cms.double(1.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip3dSig'),
    useExternalSV = cms.bool(True),
    usePVError = cms.bool(True),
    vertexCuts = cms.PSet(
        distSig2dMax = cms.double(99999.9),
        distSig2dMin = cms.double(2.0),
        distSig3dMax = cms.double(99999.9),
        distSig3dMin = cms.double(-99999.9),
        distVal2dMax = cms.double(2.5),
        distVal2dMin = cms.double(0.01),
        distVal3dMax = cms.double(99999.9),
        distVal3dMin = cms.double(-99999.9),
        fracPV = cms.double(0.79),
        massMax = cms.double(6.5),
        maxDeltaRToJetAxis = cms.double(0.4),
        minimumTrackWeight = cms.double(0.5),
        multiplicityMin = cms.uint32(2),
        useTrackWeights = cms.bool(True),
        v0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        )
    ),
    vertexReco = cms.PSet(
        finder = cms.string('avr'),
        minweight = cms.double(0.5),
        primcut = cms.double(1.8),
        seccut = cms.double(6.0),
        smoothing = cms.bool(False),
        weightthreshold = cms.double(0.001)
    ),
    vertexSelection = cms.PSet(
        sortCriterium = cms.string('dist3dError')
    )
)


process.photonIDValueMapProducer = cms.EDProducer("PhotonIDValueMapProducer",
    ebReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEB"),
    ebReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEBRecHits"),
    eeReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsEE"),
    eeReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedEERecHits"),
    esReducedRecHitCollection = cms.InputTag("reducedEcalRecHitsES"),
    esReducedRecHitCollectionMiniAOD = cms.InputTag("reducedEgamma","reducedESRecHits"),
    particleBasedIsolation = cms.InputTag("particleBasedIsolation","gedPhotons"),
    pfCandidates = cms.InputTag("particleFlow"),
    pfCandidatesMiniAOD = cms.InputTag("packedPFCandidates"),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons"),
    vertices = cms.InputTag("offlinePrimaryVertices"),
    verticesMiniAOD = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.photonMVAValueMapProducer = cms.EDProducer("PhotonMVAValueMapProducer",
    mvaConfigurations = cms.VPSet(
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            effAreasConfigFile = cms.FileInPath('RecoEgamma/PhotonIdentification/data/Spring16/effAreaPhotons_cone03_pfPhotons_90percentBased_3bins.txt'),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('Run2Spring16NonTrigV1'),
            nCategories = cms.int32(2),
            phoIsoCutoff = cms.double(2.5),
            phoIsoPtScalingCoeff = cms.vdouble(0.0053, 0.0034),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesSpring16.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Spring16/EE_V1.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v1p1'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V1.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V1.weights.xml.gz'
            )
        ), 
        cms.PSet(
            categoryCuts = cms.vstring(
                'abs(superCluster.eta) <  1.479', 
                'abs(superCluster.eta) >= 1.479'
            ),
            mvaName = cms.string('PhotonMVAEstimator'),
            mvaTag = cms.string('RunIIFall17v2'),
            nCategories = cms.int32(2),
            variableDefinition = cms.string('RecoEgamma/PhotonIdentification/data/PhotonMVAEstimatorRun2VariablesFall17V1p1.txt'),
            weightFileNames = cms.vstring(
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EB_V2.weights.xml.gz', 
                'RecoEgamma/PhotonIdentification/data/MVA/Fall17/EE_V2.weights.xml.gz'
            )
        )
    ),
    src = cms.InputTag("gedPhotons"),
    srcMiniAOD = cms.InputTag("slimmedPhotons")
)


process.pileupReweightingProducer = cms.EDProducer("PileupWeightProducer",
    PileupData = cms.vdouble(
        259000.0, 1080000.0, 2010000.0, 3780000.0, 4060000.0, 
        5880000.0, 6450000.0, 6830000.0, 9250000.0, 21800000.0, 
        43700000.0, 82700000.0, 132000000.0, 189000000.0, 266000000.0, 
        375000000.0, 524000000.0, 698000000.0, 871000000.0, 1030000000.0, 
        1170000000.0, 1290000000.0, 1370000000.0, 1440000000.0, 1500000000.0, 
        1550000000.0, 1600000000.0, 1630000000.0, 1630000000.0, 1610000000.0, 
        1570000000.0, 1510000000.0, 1430000000.0, 1340000000.0, 1240000000.0, 
        1140000000.0, 1040000000.0, 947000000.0, 866000000.0, 797000000.0, 
        744000000.0, 710000000.0, 698000000.0, 706000000.0, 730000000.0, 
        762000000.0, 791000000.0, 805000000.0, 795000000.0, 755000000.0, 
        686000000.0, 594000000.0, 491000000.0, 387000000.0, 292000000.0, 
        212000000.0, 149000000.0, 101000000.0, 66900000.0, 43400000.0, 
        27700000.0, 17500000.0, 10900000.0, 6790000.0, 4210000.0, 
        2610000.0, 1630000.0, 1030000.0, 651000.0, 418000.0, 
        271000.0, 178000.0, 117000.0, 78100.0, 52200.0, 
        35000.0, 23500.0, 15700.0, 10500.0, 6990.0, 
        4630.0, 3050.0, 2000.0, 1300.0, 844, 
        542, 345, 218, 137, 85, 
        52.3, 31.9, 19.3, 11.6, 6.85, 
        4.02, 2.34, 1.34, 0.765, 0.431
    ),
    PileupMC = cms.vdouble(
        3.39597497605e-05, 6.63688402133e-06, 1.39533611284e-05, 3.64963078209e-05, 6.00872171664e-05, 
        9.33932578027e-05, 0.000120591524486, 0.000128694546198, 0.000361697233219, 0.000361796847553, 
        0.000702474896113, 0.00133766053707, 0.00237817050805, 0.00389825605651, 0.00594546732588, 
        0.00856825906255, 0.0116627396044, 0.0148793350787, 0.0179897368379, 0.0208723871946, 
        0.0232564170641, 0.0249826433945, 0.0262245860346, 0.0272704617569, 0.0283301107549, 
        0.0294006137386, 0.0303026836965, 0.0309692426278, 0.0308818046328, 0.0310566806228, 
        0.0309692426278, 0.0310566806228, 0.0310566806228, 0.0310566806228, 0.0307696426944, 
        0.0300103336052, 0.0288355370103, 0.0273233309106, 0.0264343533951, 0.0255453758796, 
        0.0235877272306, 0.0215627588047, 0.0195825559393, 0.0177296309658, 0.0160560731931, 
        0.0146022004183, 0.0134080690078, 0.0129586991411, 0.0125093292745, 0.0124360740539, 
        0.0123547104433, 0.0123953922486, 0.0124360740539, 0.0124360740539, 0.0123547104433, 
        0.0124360740539, 0.0123387597772, 0.0122414455005, 0.011705203844, 0.0108187105305, 
        0.00963985508986, 0.00827210065136, 0.00683770076341, 0.00545237697118, 0.00420456901556, 
        0.00367513566191, 0.00314570230825, 0.0022917978982, 0.00163221454973, 0.00114065309494, 
        0.000784838366118, 0.000533204105387, 0.000358474034915, 0.000238881117601, 0.0001984254989, 
        0.000157969880198, 0.00010375646169, 6.77366175538e-05, 4.39850477645e-05, 2.84298066026e-05, 
        1.83041729561e-05, 1.17473542058e-05, 7.51982735129e-06, 6.16160108867e-06, 4.80337482605e-06, 
        3.06235473369e-06, 1.94863396999e-06, 1.23726800704e-06, 7.83538083774e-07, 4.94602064224e-07, 
        3.10989480331e-07, 1.94628487765e-07, 1.57888581037e-07, 1.2114867431e-07, 7.49518929908e-08, 
        4.6060444984e-08, 2.81008884326e-08, 1.70121486128e-08, 1.02159894812e-08
    ),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo")
)


process.probeEle = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodElectrons"),
    isAND = cms.bool(True),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.probeEleCutBasedLoose80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-loose")
)


process.probeEleCutBasedLoose94X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-loose")
)


process.probeEleCutBasedLoose94XV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleConversionVetoCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleDEtaInSeedCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleDPhiInCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleEInverseMinusPInverseCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleMissingHitsCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleRelPFIsoScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2GsfEleSCEtaMultiRangeCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedLoose94XV2MinPtCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-loose")
)


process.probeEleCutBasedMedium80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-medium")
)


process.probeEleCutBasedMedium94X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-medium")
)


process.probeEleCutBasedMedium94XV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleConversionVetoCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleDEtaInSeedCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleDPhiInCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleEInverseMinusPInverseCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleMissingHitsCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleRelPFIsoScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2GsfEleSCEtaMultiRangeCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedMedium94XV2MinPtCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-medium")
)


process.probeEleCutBasedTight80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-tight")
)


process.probeEleCutBasedTight94X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-tight")
)


process.probeEleCutBasedTight94XV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleConversionVetoCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleDEtaInSeedCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleDPhiInCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleEInverseMinusPInverseCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleMissingHitsCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleRelPFIsoScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2GsfEleSCEtaMultiRangeCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedTight94XV2MinPtCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.probeEleCutBasedVeto80X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Summer16-80X-V1-veto")
)


process.probeEleCutBasedVeto94X = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V1-veto")
)


process.probeEleCutBasedVeto94XV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleConversionVetoCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleDEtaInSeedCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleDPhiInCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleEInverseMinusPInverseCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleMissingHitsCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleRelPFIsoScaledCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2GsfEleSCEtaMultiRangeCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleCutBasedVeto94XV2MinPtCut = cms.EDProducer("PatElectronNm1Selector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    cutNamesToMask = cms.vstring(
        'GsfEleSCEtaMultiRangeCut_0', 
        'GsfEleDEtaInSeedCut_0', 
        'GsfEleDPhiInCut_0', 
        'GsfEleFull5x5SigmaIEtaIEtaCut_0', 
        'GsfEleHadronicOverEMEnergyScaledCut_0', 
        'GsfEleEInverseMinusPInverseCut_0', 
        'GsfEleRelPFIsoScaledCut_0', 
        'GsfEleConversionVetoCut_0', 
        'GsfEleMissingHitsCut_0'
    ),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-veto")
)


process.probeEleDoubleEleHLTsafe = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedDoubleElectronHLTPreselection-Summer16-V1")
)


process.probeEleHLTsafe = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronHLTPreselection-Summer16-V1")
)


process.probeEleL1matched = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodElectronProbesL1"),
    isAND = cms.bool(True),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.probeEleMVA80Xwp80 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp80")
)


process.probeEleMVA80Xwp90 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Spring16-GeneralPurpose-V1-wp90")
)


process.probeEleMVA94Xwp80iso = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp80")
)


process.probeEleMVA94Xwp80isoV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp80")
)


process.probeEleMVA94Xwp80noiso = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp80")
)


process.probeEleMVA94Xwp80noisoV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp80")
)


process.probeEleMVA94Xwp90iso = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wp90")
)


process.probeEleMVA94Xwp90isoV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wp90")
)


process.probeEleMVA94Xwp90noiso = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wp90")
)


process.probeEleMVA94Xwp90noisoV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wp90")
)


process.probeEleMVA94XwpHZZisoV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpHZZ")
)


process.probeEleMVA94XwpLooseiso = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V1-wpLoose")
)


process.probeEleMVA94XwpLooseisoV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-iso-V2-wpLoose")
)


process.probeEleMVA94XwpLoosenoiso = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V1-wpLoose")
)


process.probeEleMVA94XwpLoosenoisoV2 = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","mvaEleID-Fall17-noIso-V2-wpLoose")
)


process.probeElePassHLT = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(
        'hltEle32L1DoubleEGWPTightGsfTrackIsoFilter', 
        'hltEGL1SingleEGOrFilter'
    ),
    inputs = cms.InputTag("probeEle"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.probeElePassHLTL1matched = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(
        'hltEle32L1DoubleEGWPTightGsfTrackIsoFilter', 
        'hltEGL1SingleEGOrFilter'
    ),
    inputs = cms.InputTag("probeEleL1matched"),
    isAND = cms.bool(False),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.probePho = cms.EDProducer("PatPhotonTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodPhotons"),
    isAND = cms.bool(True),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.probePhoCutBasedLoose80X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-loose")
)


process.probePhoCutBasedLoose94X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-loose")
)


process.probePhoCutBasedLoose94XV2 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedLoose94XV2MinPtCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedLoose94XV2PhoFull5x5SigmaIEtaIEtaCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut1 = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut2 = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedLoose94XV2PhoSCEtaMultiRangeCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedLoose94XV2PhoSingleTowerHadOverEmCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-loose")
)


process.probePhoCutBasedMedium80X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-medium")
)


process.probePhoCutBasedMedium94X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-medium")
)


process.probePhoCutBasedMedium94XV2 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedMedium94XV2MinPtCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedMedium94XV2PhoFull5x5SigmaIEtaIEtaCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut1 = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut2 = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedMedium94XV2PhoSCEtaMultiRangeCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedMedium94XV2PhoSingleTowerHadOverEmCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-medium")
)


process.probePhoCutBasedTight80X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Spring16-V2p2-tight")
)


process.probePhoCutBasedTight94X = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V1-tight")
)


process.probePhoCutBasedTight94XV2 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoCutBasedTight94XV2MinPtCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoCutBasedTight94XV2PhoFull5x5SigmaIEtaIEtaCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut1 = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut2 = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoCutBasedTight94XV2PhoSCEtaMultiRangeCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSingleTowerHadOverEmCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoCutBasedTight94XV2PhoSingleTowerHadOverEmCut = cms.EDProducer("PatPhotonNm1Selector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    cutNamesToMask = cms.vstring(
        'MinPtCut_0', 
        'PhoSCEtaMultiRangeCut_0', 
        'PhoFull5x5SigmaIEtaIEtaCut_0', 
        'PhoGenericRhoPtScaledCut_0', 
        'PhoGenericRhoPtScaledCut_1', 
        'PhoGenericRhoPtScaledCut_2'
    ),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","cutBasedPhotonID-Fall17-94X-V2-tight")
)


process.probePhoMVA80Xwp80 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp80")
)


process.probePhoMVA80Xwp90 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","mvaPhoID-Spring16-nonTrig-V1-wp90")
)


process.probePhoMVA94XV2wp80 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp80")
)


process.probePhoMVA94XV2wp90 = cms.EDProducer("PatPhotonSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodPhotons"),
    selection = cms.InputTag("egmPhotonIDs","mvaPhoID-RunIIFall17-v2-wp90")
)


process.probeSC = cms.EDProducer("RecoEcalCandidateTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(),
    inputs = cms.InputTag("goodSuperClusters"),
    isAND = cms.bool(True),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.probeSCEle = cms.EDProducer("PatElectronMatchedCandidateProducer",
    ReferenceElectronCollection = cms.untracked.InputTag("goodElectrons"),
    cut = cms.string('abs(eta)<2.5 &&  et>5.0'),
    src = cms.InputTag("superClusterCands")
)


process.ptRatioRelForEle = cms.EDProducer("ElectronJetVarProducer",
    srcJet = cms.InputTag("selectedUpdatedPatJetsUpdated"),
    srcLep = cms.InputTag("slimmedElectrons"),
    srcVtx = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.randomEngineStateProducer = cms.EDProducer("RandomEngineStateProducer")


process.superClusterCands = cms.EDProducer("ConcreteEcalCandidateProducer",
    particleType = cms.int32(11),
    src = cms.InputTag("reducedEgamma","reducedSuperClusters")
)


process.tagEle = cms.EDProducer("PatElectronTriggerCandProducer",
    bits = cms.InputTag("TriggerResults","","HLT"),
    dR = cms.double(0.3),
    filterNames = cms.vstring(
        'hltEle32L1DoubleEGWPTightGsfTrackIsoFilter', 
        'hltEGL1SingleEGOrFilter'
    ),
    inputs = cms.InputTag("tagEleCutBasedTight"),
    isAND = cms.bool(True),
    objects = cms.InputTag("slimmedPatTrigger")
)


process.tagEleCutBasedTight = cms.EDProducer("PatElectronSelectorByValueMap",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.1) && !(1.4442<=abs(-log(tan(superClusterPosition.theta/2)))<=1.566) && pt >= 30.0'),
    id_cut = cms.bool(True),
    input = cms.InputTag("goodElectrons"),
    selection = cms.InputTag("egmGsfElectronIDs","cutBasedElectronID-Fall17-94X-V2-tight")
)


process.tnpPairingEleHLT = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(True),
    cut = cms.string('50<mass<130'),
    decay = cms.string('tagEle@+ probeEle@-')
)


process.tnpPairingEleIDs = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('50<mass<130'),
    decay = cms.string('tagEle probeEle')
)


process.tnpPairingEleRec = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('50<mass<130'),
    decay = cms.string('tagEle probeSC')
)


process.tnpPairingPhoIDs = cms.EDProducer("CandViewShallowCloneCombiner",
    checkCharge = cms.bool(False),
    cut = cms.string('50<mass<130'),
    decay = cms.string('tagEle probePho')
)


process.updatedPatJetsTransientCorrectedUpdated = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(cms.InputTag("pfDeepFlavourJetTagsUpdated","problepb"), cms.InputTag("pfDeepFlavourJetTagsUpdated","probbb"), cms.InputTag("pfDeepFlavourJetTagsUpdated","probb")),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsTransientCorrectedUpdated")),
    jetSource = cms.InputTag("updatedPatJetsUpdated"),
    printWarning = cms.bool(True),
    tagInfoSources = cms.VInputTag(cms.InputTag("pfDeepFlavourTagInfosUpdated"), cms.InputTag("pfDeepCSVTagInfosUpdated"), cms.InputTag("pfImpactParameterTagInfosUpdated"), cms.InputTag("pfInclusiveSecondaryVertexFinderTagInfosUpdated")),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.updatedPatJetsUpdated = cms.EDProducer("PATJetUpdater",
    addBTagInfo = cms.bool(True),
    addDiscriminators = cms.bool(True),
    addJetCorrFactors = cms.bool(True),
    addTagInfos = cms.bool(False),
    discriminatorSources = cms.VInputTag(),
    jetCorrFactorsSource = cms.VInputTag(cms.InputTag("patJetCorrFactorsUpdated")),
    jetSource = cms.InputTag("slimmedJets"),
    printWarning = cms.bool(True),
    tagInfoSources = cms.VInputTag(),
    userData = cms.PSet(
        userCands = cms.PSet(
            src = cms.VInputTag("")
        ),
        userClasses = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFloats = cms.PSet(
            src = cms.VInputTag("")
        ),
        userFunctionLabels = cms.vstring(),
        userFunctions = cms.vstring(),
        userInts = cms.PSet(
            src = cms.VInputTag("")
        )
    )
)


process.genEle = cms.EDFilter("GenParticleSelector",
    cut = cms.string('abs(pdgId) == 11 && pt > 3 && abs(eta) < 2.7 && isPromptFinalState'),
    src = cms.InputTag("prunedGenParticles")
)


process.goodElectrons = cms.EDFilter("PATElectronRefSelector",
    cut = cms.string('ecalEnergy*sin(superClusterPosition.theta)>5.0 &&  (abs(-log(tan(superClusterPosition.theta/2)))<2.5)'),
    src = cms.InputTag("slimmedElectrons")
)


process.goodPhotons = cms.EDFilter("PATPhotonRefSelector",
    cut = cms.string('(abs(-log(tan(superCluster.position.theta/2)))<=2.5) && pt> 10'),
    src = cms.InputTag("slimmedPhotons")
)


process.goodSuperClusters = cms.EDFilter("RecoEcalCandidateRefSelector",
    cut = cms.string('abs(eta)<2.5 &&  et>5.0'),
    filter = cms.bool(True),
    src = cms.InputTag("superClusterCands")
)


process.hltFilter = cms.EDFilter("HLTHighLevel",
    HLTPaths = cms.vstring('HLT_Ele32_WPTight_Gsf_L1DoubleEG_v*'),
    TriggerResultsTag = cms.InputTag("TriggerResults","","HLT"),
    andOr = cms.bool(True),
    eventSetupPathsKey = cms.string(''),
    throw = cms.bool(True)
)


process.selectedUpdatedPatJetsUpdated = cms.EDFilter("PATJetSelector",
    cut = cms.string(''),
    cutLoose = cms.string(''),
    nLoose = cms.uint32(0),
    src = cms.InputTag("updatedPatJetsTransientCorrectedUpdated")
)


process.evtCounter = cms.EDAnalyzer("SimpleEventCounter")


process.tnpEleIDs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    PUWeightSrc = cms.InputTag("pileupReweightingProducer","pileupWeights"),
    addCaloMet = cms.bool(False),
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("probeEle"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    eventWeight = cms.InputTag("generator"),
    flags = cms.PSet(
        passingCutBasedLoose80X = cms.InputTag("probeEleCutBasedLoose80X"),
        passingCutBasedLoose94X = cms.InputTag("probeEleCutBasedLoose94X"),
        passingCutBasedLoose94XV2 = cms.InputTag("probeEleCutBasedLoose94XV2"),
        passingCutBasedLoose94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleConversionVetoCut"),
        passingCutBasedLoose94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedLoose94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleDPhiInCut"),
        passingCutBasedLoose94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedLoose94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedLoose94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedLoose94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleMissingHitsCut"),
        passingCutBasedLoose94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedLoose94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedLoose94XV2MinPtCut = cms.InputTag("probeEleCutBasedLoose94XV2MinPtCut"),
        passingCutBasedMedium80X = cms.InputTag("probeEleCutBasedMedium80X"),
        passingCutBasedMedium94X = cms.InputTag("probeEleCutBasedMedium94X"),
        passingCutBasedMedium94XV2 = cms.InputTag("probeEleCutBasedMedium94XV2"),
        passingCutBasedMedium94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleConversionVetoCut"),
        passingCutBasedMedium94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedMedium94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleDPhiInCut"),
        passingCutBasedMedium94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedMedium94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedMedium94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedMedium94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleMissingHitsCut"),
        passingCutBasedMedium94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedMedium94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedMedium94XV2MinPtCut = cms.InputTag("probeEleCutBasedMedium94XV2MinPtCut"),
        passingCutBasedTight80X = cms.InputTag("probeEleCutBasedTight80X"),
        passingCutBasedTight94X = cms.InputTag("probeEleCutBasedTight94X"),
        passingCutBasedTight94XV2 = cms.InputTag("probeEleCutBasedTight94XV2"),
        passingCutBasedTight94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleConversionVetoCut"),
        passingCutBasedTight94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedTight94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleDPhiInCut"),
        passingCutBasedTight94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedTight94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedTight94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedTight94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleMissingHitsCut"),
        passingCutBasedTight94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedTight94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedTight94XV2MinPtCut = cms.InputTag("probeEleCutBasedTight94XV2MinPtCut"),
        passingCutBasedVeto80X = cms.InputTag("probeEleCutBasedVeto80X"),
        passingCutBasedVeto94X = cms.InputTag("probeEleCutBasedVeto94X"),
        passingCutBasedVeto94XV2 = cms.InputTag("probeEleCutBasedVeto94XV2"),
        passingCutBasedVeto94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleConversionVetoCut"),
        passingCutBasedVeto94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedVeto94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleDPhiInCut"),
        passingCutBasedVeto94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedVeto94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedVeto94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedVeto94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleMissingHitsCut"),
        passingCutBasedVeto94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedVeto94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedVeto94XV2MinPtCut = cms.InputTag("probeEleCutBasedVeto94XV2MinPtCut"),
        passingDoubleEleHLTsafe = cms.InputTag("probeEleDoubleEleHLTsafe"),
        passingHLTsafe = cms.InputTag("probeEleHLTsafe"),
        passingMVA80Xwp80 = cms.InputTag("probeEleMVA80Xwp80"),
        passingMVA80Xwp90 = cms.InputTag("probeEleMVA80Xwp90"),
        passingMVA94Xwp80iso = cms.InputTag("probeEleMVA94Xwp80iso"),
        passingMVA94Xwp80isoV2 = cms.InputTag("probeEleMVA94Xwp80isoV2"),
        passingMVA94Xwp80noiso = cms.InputTag("probeEleMVA94Xwp80noiso"),
        passingMVA94Xwp80noisoV2 = cms.InputTag("probeEleMVA94Xwp80noisoV2"),
        passingMVA94Xwp90iso = cms.InputTag("probeEleMVA94Xwp90iso"),
        passingMVA94Xwp90isoV2 = cms.InputTag("probeEleMVA94Xwp90isoV2"),
        passingMVA94Xwp90noiso = cms.InputTag("probeEleMVA94Xwp90noiso"),
        passingMVA94Xwp90noisoV2 = cms.InputTag("probeEleMVA94Xwp90noisoV2"),
        passingMVA94XwpHZZisoV2 = cms.InputTag("probeEleMVA94XwpHZZisoV2"),
        passingMVA94XwpLooseiso = cms.InputTag("probeEleMVA94XwpLooseiso"),
        passingMVA94XwpLooseisoV2 = cms.InputTag("probeEleMVA94XwpLooseisoV2"),
        passingMVA94XwpLoosenoiso = cms.InputTag("probeEleMVA94XwpLoosenoiso"),
        passingMVA94XwpLoosenoisoV2 = cms.InputTag("probeEleMVA94XwpLoosenoisoV2")
    ),
    isMC = cms.bool(True),
    makeMCUnbiasTree = cms.bool(False),
    mcFlags = cms.PSet(
        probe_flag = cms.string('pt>0')
    ),
    mcVariables = cms.PSet(
        probe_e = cms.string('energy'),
        probe_et = cms.string('et'),
        probe_eta = cms.string('eta'),
        probe_phi = cms.string('phi')
    ),
    motherPdgId = cms.vint32(),
    pairFlags = cms.PSet(

    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    probeMatches = cms.InputTag("genProbeEle"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagMatches = cms.InputTag("genTagEle"),
    tagProbePairs = cms.InputTag("tnpPairingEleIDs"),
    tagVariables = cms.PSet(
        Ele_1overEminus1overP = cms.string('abs(1-eSuperClusterOverP())/ecalEnergy()'),
        Ele_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        Ele_5x5_sieie = cms.string('full5x5_showerShape().sigmaIetaIeta'),
        Ele_IsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        Ele_IsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        Ele_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_hoe = cms.string('hadronicOverEm()'),
        Ele_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        Ele_idCutForTrigger = cms.InputTag("eleVarHelper","idCutForTrigger"),
        Ele_ip2D = cms.InputTag("eleVarHelper","ip2D"),
        Ele_ipDZ = cms.InputTag("eleVarHelper","ipDZ"),
        Ele_isPOGIP = cms.InputTag("eleVarHelper","isPOGIP"),
        Ele_isPOGIP2D = cms.InputTag("eleVarHelper","isPOGIP2D"),
        Ele_isoCutForTrigger = cms.InputTag("eleVarHelper","isoCutForTrigger"),
        Ele_noIsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
        Ele_noIsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
        Ele_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_relEcalIso = cms.InputTag("eleVarHelper","relEcalIso"),
        Ele_relHcalIso = cms.InputTag("eleVarHelper","relHcalIso"),
        Ele_relPFIso = cms.InputTag("eleVarHelper","relPFIso"),
        Ele_relTrkIso = cms.InputTag("eleVarHelper","relTrkIso"),
        Ele_sip = cms.InputTag("eleVarHelper","sip"),
        Ele_sip2D = cms.InputTag("eleVarHelper","sip2D"),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_e = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        el_1overEminus1overP = cms.string('abs(1-eSuperClusterOverP())/ecalEnergy()'),
        el_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        el_5x5_circularity = cms.InputTag("eleVarHelper","5x5circularity"),
        el_5x5_e1x5 = cms.string('full5x5_showerShape().e1x5'),
        el_5x5_e2x5 = cms.string('full5x5_showerShape().e2x5Max'),
        el_5x5_e5x5 = cms.string('full5x5_showerShape().e5x5'),
        el_5x5_hoe = cms.string('full5x5_hcalOverEcal()'),
        el_5x5_r9 = cms.string('full5x5_showerShape().r9'),
        el_5x5_sieie = cms.string('full5x5_showerShape().sigmaIetaIeta'),
        el_5x5_sieip = cms.string('full5x5_showerShape().sigmaIetaIphi'),
        el_IoEmIop = cms.InputTag("eleVarHelper","ioemiop"),
        el_IsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1RawValues"),
        el_IsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
        el_abseta = cms.string('abs(eta)'),
        el_chIso = cms.string('pfIsolationVariables().sumChargedHadronPt'),
        el_closestJetDeepCsv = cms.InputTag("leptonMvaTOP","closestJetDeepCsv"),
        el_closestJetDeepFlavour = cms.InputTag("leptonMvaTOP","closestJetDeepFlavour"),
        el_convVtxFitProb = cms.InputTag("eleVarHelper","convVtxFitProb"),
        el_dEtaIn = cms.string('deltaEtaSuperClusterTrackAtVtx'),
        el_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        el_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        el_dr03EcalRecHitSumEt = cms.string('dr03EcalRecHitSumEt'),
        el_dr03TkSumPt = cms.string('dr03TkSumPt'),
        el_dxy = cms.InputTag("eleVarHelper","dxy"),
        el_dz = cms.InputTag("eleVarHelper","dz"),
        el_e = cms.string('energy'),
        el_e1x5 = cms.string('showerShape().e1x5'),
        el_e2x5 = cms.string('showerShape().e2x5Max'),
        el_e5x5 = cms.string('showerShape().e5x5'),
        el_ecalDriven = cms.string('ecalDrivenSeed'),
        el_ecalEnergy = cms.string('ecalEnergy()'),
        el_ecalIso = cms.string('ecalPFClusterIso'),
        el_eelepout = cms.string('eEleClusterOverPout()'),
        el_eoverp_wES = cms.string('(superCluster().rawEnergy+superCluster().preshowerEnergy)/gsfTrack().pMode()'),
        el_ep = cms.string('eSuperClusterOverP()'),
        el_et = cms.string('et'),
        el_eta = cms.string('eta'),
        el_etaW = cms.string('superCluster().etaWidth'),
        el_fbrem = cms.string('fbrem'),
        el_found_hits = cms.string('gsfTrack().found()'),
        el_gsfHits = cms.InputTag("eleVarHelper","gsfhits"),
        el_gsfchi2 = cms.string('gsfTrack().normalizedChi2()'),
        el_gsfhits = cms.string('gsfTrack().hitPattern().trackerLayersWithMeasurement()'),
        el_hasMatchedConversion = cms.InputTag("eleVarHelper","hasMatchedConversion"),
        el_hcalIso = cms.string('hcalPFClusterIso'),
        el_hoe = cms.string('hadronicOverEm()'),
        el_hoe_bc = cms.string('hcalOverEcalBc'),
        el_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        el_idCutForTrigger = cms.InputTag("eleVarHelper","idCutForTrigger"),
        el_ip2D = cms.InputTag("eleVarHelper","ip2D"),
        el_ipDZ = cms.InputTag("eleVarHelper","ipDZ"),
        el_isGap = cms.string('isGap'),
        el_isPOGIP = cms.InputTag("eleVarHelper","isPOGIP"),
        el_isPOGIP2D = cms.InputTag("eleVarHelper","isPOGIP2D"),
        el_isoCutForTrigger = cms.InputTag("eleVarHelper","isoCutForTrigger"),
        el_kfchi2 = cms.InputTag("eleVarHelper","kfchi2"),
        el_kfhits = cms.InputTag("eleVarHelper","kfhits"),
        el_leptonMva_TOP = cms.InputTag("leptonMvaTOP","leptonMvaTOP"),
        el_leptonMva_ghent = cms.InputTag("leptonMvaGhent","leptonMvaGhent"),
        el_leptonMva_ttH = cms.InputTag("leptonMvaTTH","leptonMvaTTH"),
        el_lost_hits = cms.string('gsfTrack().lost()'),
        el_mHits = cms.InputTag("eleVarHelper","missinghits"),
        el_miniIsoAll_fall17 = cms.InputTag("isoForEleFall17","miniIsoAll"),
        el_miniIsoChg_fall17 = cms.InputTag("isoForEleFall17","miniIsoChg"),
        el_neuIso = cms.string('pfIsolationVariables().sumNeutralHadronEt'),
        el_noIsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
        el_noIsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
        el_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        el_pf_pt = cms.InputTag("eleVarHelper","pfPt"),
        el_phi = cms.string('phi'),
        el_phiW = cms.string('superCluster().phiWidth'),
        el_phoIso = cms.string('pfIsolationVariables().sumPhotonEt'),
        el_pt = cms.string('pt'),
        el_ptRatio = cms.InputTag("ptRatioRelForEle","ptRatio"),
        el_ptRel = cms.InputTag("ptRatioRelForEle","ptRel"),
        el_q = cms.string('charge'),
        el_r9 = cms.string('showerShape().r9'),
        el_relEcalIso = cms.InputTag("eleVarHelper","relEcalIso"),
        el_relHcalIso = cms.InputTag("eleVarHelper","relHcalIso"),
        el_relIso03_dB = cms.string('(pfIsolationVariables().sumChargedHadronPt + max(pfIsolationVariables().sumNeutralHadronEt + pfIsolationVariables().sumPhotonEt - 0.5 * pfIsolationVariables().sumPUPt,0.0)) / pt() '),
        el_relIso_fall17 = cms.InputTag("isoForEleFall17","PFIsoAll"),
        el_relPFIso = cms.InputTag("eleVarHelper","relPFIso"),
        el_relPfLepIso03 = cms.InputTag("eleVarHelper","pfLeptonIsolation"),
        el_relTrkIso = cms.InputTag("eleVarHelper","relTrkIso"),
        el_sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        el_sc_e = cms.string('superCluster().energy'),
        el_sc_esE = cms.string('superCluster().preshowerEnergy'),
        el_sc_et = cms.string('superCluster().energy*sin(superClusterPosition.theta)'),
        el_sc_eta = cms.string('-log(tan(superCluster.position.theta/2))'),
        el_sc_phi = cms.string('superCluster.phi'),
        el_sc_rawE = cms.string('superCluster().rawEnergy'),
        el_seed_e = cms.string('superCluster.seed.energy'),
        el_sieie = cms.string('showerShape().sigmaIetaIeta'),
        el_sip = cms.InputTag("eleVarHelper","sip"),
        el_sip2D = cms.InputTag("eleVarHelper","sip2D"),
        el_sumPUPt = cms.string('pfIsolationVariables().sumPUPt'),
        el_tk_eta = cms.string('gsfTrack().etaMode'),
        el_tk_phi = cms.string('gsfTrack().phiMode'),
        el_tk_pt = cms.string('gsfTrack().ptMode'),
        el_trkIso = cms.string('trackIso')
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.tnpEleReco = cms.EDAnalyzer("TagProbeFitTreeProducer",
    PUWeightSrc = cms.InputTag("pileupReweightingProducer","pileupWeights"),
    addCaloMet = cms.bool(False),
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("probeSC"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    eventWeight = cms.InputTag("generator"),
    flags = cms.PSet(
        passingRECO = cms.InputTag("probeSCEle","superclusters"),
        passingRECOEcalDriven = cms.InputTag("probeSCEle","superclustersEcalDriven"),
        passingRECOTrackDriven = cms.InputTag("probeSCEle","superclustersTrackDriven")
    ),
    isMC = cms.bool(True),
    makeMCUnbiasTree = cms.bool(False),
    mcFlags = cms.PSet(
        probe_flag = cms.string('pt>0')
    ),
    mcVariables = cms.PSet(
        probe_e = cms.string('energy'),
        probe_et = cms.string('et'),
        probe_eta = cms.string('eta'),
        probe_phi = cms.string('phi')
    ),
    motherPdgId = cms.vint32(),
    pairFlags = cms.PSet(

    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    probeMatches = cms.InputTag("genProbeSC"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagMatches = cms.InputTag("genTagEle"),
    tagProbePairs = cms.InputTag("tnpPairingEleRec"),
    tagVariables = cms.PSet(
        Ele_1overEminus1overP = cms.string('abs(1-eSuperClusterOverP())/ecalEnergy()'),
        Ele_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        Ele_5x5_sieie = cms.string('full5x5_showerShape().sigmaIetaIeta'),
        Ele_IsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        Ele_IsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        Ele_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_hoe = cms.string('hadronicOverEm()'),
        Ele_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        Ele_idCutForTrigger = cms.InputTag("eleVarHelper","idCutForTrigger"),
        Ele_ip2D = cms.InputTag("eleVarHelper","ip2D"),
        Ele_ipDZ = cms.InputTag("eleVarHelper","ipDZ"),
        Ele_isPOGIP = cms.InputTag("eleVarHelper","isPOGIP"),
        Ele_isPOGIP2D = cms.InputTag("eleVarHelper","isPOGIP2D"),
        Ele_isoCutForTrigger = cms.InputTag("eleVarHelper","isoCutForTrigger"),
        Ele_noIsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
        Ele_noIsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
        Ele_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_relEcalIso = cms.InputTag("eleVarHelper","relEcalIso"),
        Ele_relHcalIso = cms.InputTag("eleVarHelper","relHcalIso"),
        Ele_relPFIso = cms.InputTag("eleVarHelper","relPFIso"),
        Ele_relTrkIso = cms.InputTag("eleVarHelper","relTrkIso"),
        Ele_sip = cms.InputTag("eleVarHelper","sip"),
        Ele_sip2D = cms.InputTag("eleVarHelper","sip2D"),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_e = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        sc_abseta = cms.string('abs(eta)'),
        sc_e = cms.string('energy'),
        sc_et = cms.string('et'),
        sc_eta = cms.string('eta'),
        sc_phi = cms.string('phi'),
        sc_pt = cms.string('pt'),
        sc_tkIso = cms.InputTag("recoEcalCandidateHelper","scTkIso")
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.tnpEleTrig = cms.EDAnalyzer("TagProbeFitTreeProducer",
    PUWeightSrc = cms.InputTag("pileupReweightingProducer","pileupWeights"),
    addCaloMet = cms.bool(False),
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("probeEle"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    eventWeight = cms.InputTag("generator"),
    flags = cms.PSet(
        passEGL1SingleEGOr = cms.InputTag("passEGL1SingleEGOr"),
        passHltDoubleEle33CaloIdLMWSeedLegL1match = cms.InputTag("passHltDoubleEle33CaloIdLMWSeedLegL1match"),
        passHltDoubleEle33CaloIdLMWUnsLeg = cms.InputTag("passHltDoubleEle33CaloIdLMWUnsLeg"),
        passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match = cms.InputTag("passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match"),
        passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2 = cms.InputTag("passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2"),
        passHltEle32DoubleEGWPTightGsf = cms.InputTag("passHltEle32DoubleEGWPTightGsf"),
        passingCutBasedLoose80X = cms.InputTag("probeEleCutBasedLoose80X"),
        passingCutBasedLoose94X = cms.InputTag("probeEleCutBasedLoose94X"),
        passingCutBasedLoose94XV2 = cms.InputTag("probeEleCutBasedLoose94XV2"),
        passingCutBasedLoose94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleConversionVetoCut"),
        passingCutBasedLoose94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedLoose94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleDPhiInCut"),
        passingCutBasedLoose94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedLoose94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedLoose94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedLoose94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleMissingHitsCut"),
        passingCutBasedLoose94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedLoose94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedLoose94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedLoose94XV2MinPtCut = cms.InputTag("probeEleCutBasedLoose94XV2MinPtCut"),
        passingCutBasedMedium80X = cms.InputTag("probeEleCutBasedMedium80X"),
        passingCutBasedMedium94X = cms.InputTag("probeEleCutBasedMedium94X"),
        passingCutBasedMedium94XV2 = cms.InputTag("probeEleCutBasedMedium94XV2"),
        passingCutBasedMedium94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleConversionVetoCut"),
        passingCutBasedMedium94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedMedium94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleDPhiInCut"),
        passingCutBasedMedium94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedMedium94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedMedium94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedMedium94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleMissingHitsCut"),
        passingCutBasedMedium94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedMedium94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedMedium94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedMedium94XV2MinPtCut = cms.InputTag("probeEleCutBasedMedium94XV2MinPtCut"),
        passingCutBasedTight80X = cms.InputTag("probeEleCutBasedTight80X"),
        passingCutBasedTight94X = cms.InputTag("probeEleCutBasedTight94X"),
        passingCutBasedTight94XV2 = cms.InputTag("probeEleCutBasedTight94XV2"),
        passingCutBasedTight94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleConversionVetoCut"),
        passingCutBasedTight94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedTight94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleDPhiInCut"),
        passingCutBasedTight94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedTight94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedTight94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedTight94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleMissingHitsCut"),
        passingCutBasedTight94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedTight94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedTight94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedTight94XV2MinPtCut = cms.InputTag("probeEleCutBasedTight94XV2MinPtCut"),
        passingCutBasedVeto80X = cms.InputTag("probeEleCutBasedVeto80X"),
        passingCutBasedVeto94X = cms.InputTag("probeEleCutBasedVeto94X"),
        passingCutBasedVeto94XV2 = cms.InputTag("probeEleCutBasedVeto94XV2"),
        passingCutBasedVeto94XV2GsfEleConversionVetoCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleConversionVetoCut"),
        passingCutBasedVeto94XV2GsfEleDEtaInSeedCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleDEtaInSeedCut"),
        passingCutBasedVeto94XV2GsfEleDPhiInCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleDPhiInCut"),
        passingCutBasedVeto94XV2GsfEleEInverseMinusPInverseCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleEInverseMinusPInverseCut"),
        passingCutBasedVeto94XV2GsfEleFull5x5SigmaIEtaIEtaCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedVeto94XV2GsfEleHadronicOverEMEnergyScaledCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleHadronicOverEMEnergyScaledCut"),
        passingCutBasedVeto94XV2GsfEleMissingHitsCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleMissingHitsCut"),
        passingCutBasedVeto94XV2GsfEleRelPFIsoScaledCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleRelPFIsoScaledCut"),
        passingCutBasedVeto94XV2GsfEleSCEtaMultiRangeCut = cms.InputTag("probeEleCutBasedVeto94XV2GsfEleSCEtaMultiRangeCut"),
        passingCutBasedVeto94XV2MinPtCut = cms.InputTag("probeEleCutBasedVeto94XV2MinPtCut"),
        passingDoubleEleHLTsafe = cms.InputTag("probeEleDoubleEleHLTsafe"),
        passingHLTsafe = cms.InputTag("probeEleHLTsafe"),
        passingMVA80Xwp80 = cms.InputTag("probeEleMVA80Xwp80"),
        passingMVA80Xwp90 = cms.InputTag("probeEleMVA80Xwp90"),
        passingMVA94Xwp80iso = cms.InputTag("probeEleMVA94Xwp80iso"),
        passingMVA94Xwp80isoV2 = cms.InputTag("probeEleMVA94Xwp80isoV2"),
        passingMVA94Xwp80noiso = cms.InputTag("probeEleMVA94Xwp80noiso"),
        passingMVA94Xwp80noisoV2 = cms.InputTag("probeEleMVA94Xwp80noisoV2"),
        passingMVA94Xwp90iso = cms.InputTag("probeEleMVA94Xwp90iso"),
        passingMVA94Xwp90isoV2 = cms.InputTag("probeEleMVA94Xwp90isoV2"),
        passingMVA94Xwp90noiso = cms.InputTag("probeEleMVA94Xwp90noiso"),
        passingMVA94Xwp90noisoV2 = cms.InputTag("probeEleMVA94Xwp90noisoV2"),
        passingMVA94XwpHZZisoV2 = cms.InputTag("probeEleMVA94XwpHZZisoV2"),
        passingMVA94XwpLooseiso = cms.InputTag("probeEleMVA94XwpLooseiso"),
        passingMVA94XwpLooseisoV2 = cms.InputTag("probeEleMVA94XwpLooseisoV2"),
        passingMVA94XwpLoosenoiso = cms.InputTag("probeEleMVA94XwpLoosenoiso"),
        passingMVA94XwpLoosenoisoV2 = cms.InputTag("probeEleMVA94XwpLoosenoisoV2")
    ),
    isMC = cms.bool(True),
    makeMCUnbiasTree = cms.bool(False),
    mcFlags = cms.PSet(
        probe_flag = cms.string('pt>0')
    ),
    mcVariables = cms.PSet(
        probe_e = cms.string('energy'),
        probe_et = cms.string('et'),
        probe_eta = cms.string('eta'),
        probe_phi = cms.string('phi')
    ),
    motherPdgId = cms.vint32(),
    pairFlags = cms.PSet(

    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    probeMatches = cms.InputTag("genProbeEle"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagMatches = cms.InputTag("genTagEle"),
    tagProbePairs = cms.InputTag("tnpPairingEleHLT"),
    tagVariables = cms.PSet(
        Ele_1overEminus1overP = cms.string('abs(1-eSuperClusterOverP())/ecalEnergy()'),
        Ele_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        Ele_5x5_sieie = cms.string('full5x5_showerShape().sigmaIetaIeta'),
        Ele_IsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        Ele_IsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        Ele_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_hoe = cms.string('hadronicOverEm()'),
        Ele_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        Ele_idCutForTrigger = cms.InputTag("eleVarHelper","idCutForTrigger"),
        Ele_ip2D = cms.InputTag("eleVarHelper","ip2D"),
        Ele_ipDZ = cms.InputTag("eleVarHelper","ipDZ"),
        Ele_isPOGIP = cms.InputTag("eleVarHelper","isPOGIP"),
        Ele_isPOGIP2D = cms.InputTag("eleVarHelper","isPOGIP2D"),
        Ele_isoCutForTrigger = cms.InputTag("eleVarHelper","isoCutForTrigger"),
        Ele_noIsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
        Ele_noIsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
        Ele_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_relEcalIso = cms.InputTag("eleVarHelper","relEcalIso"),
        Ele_relHcalIso = cms.InputTag("eleVarHelper","relHcalIso"),
        Ele_relPFIso = cms.InputTag("eleVarHelper","relPFIso"),
        Ele_relTrkIso = cms.InputTag("eleVarHelper","relTrkIso"),
        Ele_sip = cms.InputTag("eleVarHelper","sip"),
        Ele_sip2D = cms.InputTag("eleVarHelper","sip2D"),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_e = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        el_1overEminus1overP = cms.string('abs(1-eSuperClusterOverP())/ecalEnergy()'),
        el_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        el_5x5_circularity = cms.InputTag("eleVarHelper","5x5circularity"),
        el_5x5_e1x5 = cms.string('full5x5_showerShape().e1x5'),
        el_5x5_e2x5 = cms.string('full5x5_showerShape().e2x5Max'),
        el_5x5_e5x5 = cms.string('full5x5_showerShape().e5x5'),
        el_5x5_hoe = cms.string('full5x5_hcalOverEcal()'),
        el_5x5_r9 = cms.string('full5x5_showerShape().r9'),
        el_5x5_sieie = cms.string('full5x5_showerShape().sigmaIetaIeta'),
        el_5x5_sieip = cms.string('full5x5_showerShape().sigmaIetaIphi'),
        el_IoEmIop = cms.InputTag("eleVarHelper","ioemiop"),
        el_IsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1RawValues"),
        el_IsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2RawValues"),
        el_abseta = cms.string('abs(eta)'),
        el_chIso = cms.string('pfIsolationVariables().sumChargedHadronPt'),
        el_closestJetDeepCsv = cms.InputTag("leptonMvaTOP","closestJetDeepCsv"),
        el_closestJetDeepFlavour = cms.InputTag("leptonMvaTOP","closestJetDeepFlavour"),
        el_convVtxFitProb = cms.InputTag("eleVarHelper","convVtxFitProb"),
        el_dEtaIn = cms.string('deltaEtaSuperClusterTrackAtVtx'),
        el_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        el_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        el_dr03EcalRecHitSumEt = cms.string('dr03EcalRecHitSumEt'),
        el_dr03TkSumPt = cms.string('dr03TkSumPt'),
        el_dxy = cms.InputTag("eleVarHelper","dxy"),
        el_dz = cms.InputTag("eleVarHelper","dz"),
        el_e = cms.string('energy'),
        el_e1x5 = cms.string('showerShape().e1x5'),
        el_e2x5 = cms.string('showerShape().e2x5Max'),
        el_e5x5 = cms.string('showerShape().e5x5'),
        el_ecalDriven = cms.string('ecalDrivenSeed'),
        el_ecalEnergy = cms.string('ecalEnergy()'),
        el_ecalIso = cms.string('ecalPFClusterIso'),
        el_eelepout = cms.string('eEleClusterOverPout()'),
        el_eoverp_wES = cms.string('(superCluster().rawEnergy+superCluster().preshowerEnergy)/gsfTrack().pMode()'),
        el_ep = cms.string('eSuperClusterOverP()'),
        el_et = cms.string('et'),
        el_eta = cms.string('eta'),
        el_etaW = cms.string('superCluster().etaWidth'),
        el_fbrem = cms.string('fbrem'),
        el_found_hits = cms.string('gsfTrack().found()'),
        el_gsfHits = cms.InputTag("eleVarHelper","gsfhits"),
        el_gsfchi2 = cms.string('gsfTrack().normalizedChi2()'),
        el_gsfhits = cms.string('gsfTrack().hitPattern().trackerLayersWithMeasurement()'),
        el_hasMatchedConversion = cms.InputTag("eleVarHelper","hasMatchedConversion"),
        el_hcalIso = cms.string('hcalPFClusterIso'),
        el_hoe = cms.string('hadronicOverEm()'),
        el_hoe_bc = cms.string('hcalOverEcalBc'),
        el_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        el_idCutForTrigger = cms.InputTag("eleVarHelper","idCutForTrigger"),
        el_ip2D = cms.InputTag("eleVarHelper","ip2D"),
        el_ipDZ = cms.InputTag("eleVarHelper","ipDZ"),
        el_isGap = cms.string('isGap'),
        el_isPOGIP = cms.InputTag("eleVarHelper","isPOGIP"),
        el_isPOGIP2D = cms.InputTag("eleVarHelper","isPOGIP2D"),
        el_isoCutForTrigger = cms.InputTag("eleVarHelper","isoCutForTrigger"),
        el_kfchi2 = cms.InputTag("eleVarHelper","kfchi2"),
        el_kfhits = cms.InputTag("eleVarHelper","kfhits"),
        el_leptonMva_TOP = cms.InputTag("leptonMvaTOP","leptonMvaTOP"),
        el_leptonMva_ghent = cms.InputTag("leptonMvaGhent","leptonMvaGhent"),
        el_leptonMva_ttH = cms.InputTag("leptonMvaTTH","leptonMvaTTH"),
        el_lost_hits = cms.string('gsfTrack().lost()'),
        el_mHits = cms.InputTag("eleVarHelper","missinghits"),
        el_miniIsoAll_fall17 = cms.InputTag("isoForEleFall17","miniIsoAll"),
        el_miniIsoChg_fall17 = cms.InputTag("isoForEleFall17","miniIsoChg"),
        el_neuIso = cms.string('pfIsolationVariables().sumNeutralHadronEt'),
        el_noIsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
        el_noIsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2RawValues"),
        el_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        el_pf_pt = cms.InputTag("eleVarHelper","pfPt"),
        el_phi = cms.string('phi'),
        el_phiW = cms.string('superCluster().phiWidth'),
        el_phoIso = cms.string('pfIsolationVariables().sumPhotonEt'),
        el_pt = cms.string('pt'),
        el_ptRatio = cms.InputTag("ptRatioRelForEle","ptRatio"),
        el_ptRel = cms.InputTag("ptRatioRelForEle","ptRel"),
        el_q = cms.string('charge'),
        el_r9 = cms.string('showerShape().r9'),
        el_relEcalIso = cms.InputTag("eleVarHelper","relEcalIso"),
        el_relHcalIso = cms.InputTag("eleVarHelper","relHcalIso"),
        el_relIso03_dB = cms.string('(pfIsolationVariables().sumChargedHadronPt + max(pfIsolationVariables().sumNeutralHadronEt + pfIsolationVariables().sumPhotonEt - 0.5 * pfIsolationVariables().sumPUPt,0.0)) / pt() '),
        el_relIso_fall17 = cms.InputTag("isoForEleFall17","PFIsoAll"),
        el_relPFIso = cms.InputTag("eleVarHelper","relPFIso"),
        el_relPfLepIso03 = cms.InputTag("eleVarHelper","pfLeptonIsolation"),
        el_relTrkIso = cms.InputTag("eleVarHelper","relTrkIso"),
        el_sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        el_sc_e = cms.string('superCluster().energy'),
        el_sc_esE = cms.string('superCluster().preshowerEnergy'),
        el_sc_et = cms.string('superCluster().energy*sin(superClusterPosition.theta)'),
        el_sc_eta = cms.string('-log(tan(superCluster.position.theta/2))'),
        el_sc_phi = cms.string('superCluster.phi'),
        el_sc_rawE = cms.string('superCluster().rawEnergy'),
        el_seed_e = cms.string('superCluster.seed.energy'),
        el_sieie = cms.string('showerShape().sigmaIetaIeta'),
        el_sip = cms.InputTag("eleVarHelper","sip"),
        el_sip2D = cms.InputTag("eleVarHelper","sip2D"),
        el_sumPUPt = cms.string('pfIsolationVariables().sumPUPt'),
        el_tk_eta = cms.string('gsfTrack().etaMode'),
        el_tk_phi = cms.string('gsfTrack().phiMode'),
        el_tk_pt = cms.string('gsfTrack().ptMode'),
        el_trkIso = cms.string('trackIso')
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.tnpPhoIDs = cms.EDAnalyzer("TagProbeFitTreeProducer",
    PUWeightSrc = cms.InputTag("pileupReweightingProducer","pileupWeights"),
    addCaloMet = cms.bool(False),
    addEventVariablesInfo = cms.bool(True),
    addRunLumiInfo = cms.bool(True),
    allProbes = cms.InputTag("probePho"),
    arbitration = cms.string('HighestPt'),
    beamSpot = cms.InputTag("offlineBeamSpot"),
    eventWeight = cms.InputTag("generator"),
    flags = cms.PSet(
        passingCutBasedLoose80X = cms.InputTag("probePhoCutBasedLoose80X"),
        passingCutBasedLoose94X = cms.InputTag("probePhoCutBasedLoose94X"),
        passingCutBasedLoose94XV2 = cms.InputTag("probePhoCutBasedLoose94XV2"),
        passingCutBasedLoose94XV2MinPtCut = cms.InputTag("probePhoCutBasedLoose94XV2MinPtCut"),
        passingCutBasedLoose94XV2PhoFull5x5SigmaIEtaIEtaCut = cms.InputTag("probePhoCutBasedLoose94XV2PhoFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedLoose94XV2PhoGenericRhoPtScaledCut = cms.InputTag("probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut"),
        passingCutBasedLoose94XV2PhoGenericRhoPtScaledCut1 = cms.InputTag("probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut1"),
        passingCutBasedLoose94XV2PhoGenericRhoPtScaledCut2 = cms.InputTag("probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut2"),
        passingCutBasedLoose94XV2PhoSCEtaMultiRangeCut = cms.InputTag("probePhoCutBasedLoose94XV2PhoSCEtaMultiRangeCut"),
        passingCutBasedLoose94XV2PhoSingleTowerHadOverEmCut = cms.InputTag("probePhoCutBasedLoose94XV2PhoSingleTowerHadOverEmCut"),
        passingCutBasedMedium80X = cms.InputTag("probePhoCutBasedMedium80X"),
        passingCutBasedMedium94X = cms.InputTag("probePhoCutBasedMedium94X"),
        passingCutBasedMedium94XV2 = cms.InputTag("probePhoCutBasedMedium94XV2"),
        passingCutBasedMedium94XV2MinPtCut = cms.InputTag("probePhoCutBasedMedium94XV2MinPtCut"),
        passingCutBasedMedium94XV2PhoFull5x5SigmaIEtaIEtaCut = cms.InputTag("probePhoCutBasedMedium94XV2PhoFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedMedium94XV2PhoGenericRhoPtScaledCut = cms.InputTag("probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut"),
        passingCutBasedMedium94XV2PhoGenericRhoPtScaledCut1 = cms.InputTag("probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut1"),
        passingCutBasedMedium94XV2PhoGenericRhoPtScaledCut2 = cms.InputTag("probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut2"),
        passingCutBasedMedium94XV2PhoSCEtaMultiRangeCut = cms.InputTag("probePhoCutBasedMedium94XV2PhoSCEtaMultiRangeCut"),
        passingCutBasedMedium94XV2PhoSingleTowerHadOverEmCut = cms.InputTag("probePhoCutBasedMedium94XV2PhoSingleTowerHadOverEmCut"),
        passingCutBasedTight80X = cms.InputTag("probePhoCutBasedTight80X"),
        passingCutBasedTight94X = cms.InputTag("probePhoCutBasedTight94X"),
        passingCutBasedTight94XV2 = cms.InputTag("probePhoCutBasedTight94XV2"),
        passingCutBasedTight94XV2MinPtCut = cms.InputTag("probePhoCutBasedTight94XV2MinPtCut"),
        passingCutBasedTight94XV2PhoFull5x5SigmaIEtaIEtaCut = cms.InputTag("probePhoCutBasedTight94XV2PhoFull5x5SigmaIEtaIEtaCut"),
        passingCutBasedTight94XV2PhoGenericRhoPtScaledCut = cms.InputTag("probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut"),
        passingCutBasedTight94XV2PhoGenericRhoPtScaledCut1 = cms.InputTag("probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut1"),
        passingCutBasedTight94XV2PhoGenericRhoPtScaledCut2 = cms.InputTag("probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut2"),
        passingCutBasedTight94XV2PhoSCEtaMultiRangeCut = cms.InputTag("probePhoCutBasedTight94XV2PhoSCEtaMultiRangeCut"),
        passingCutBasedTight94XV2PhoSingleTowerHadOverEmCut = cms.InputTag("probePhoCutBasedTight94XV2PhoSingleTowerHadOverEmCut"),
        passingMVA80Xwp80 = cms.InputTag("probePhoMVA80Xwp80"),
        passingMVA80Xwp90 = cms.InputTag("probePhoMVA80Xwp90"),
        passingMVA94XV2wp80 = cms.InputTag("probePhoMVA94XV2wp80"),
        passingMVA94XV2wp90 = cms.InputTag("probePhoMVA94XV2wp90")
    ),
    isMC = cms.bool(True),
    makeMCUnbiasTree = cms.bool(False),
    mcFlags = cms.PSet(
        probe_flag = cms.string('pt>0')
    ),
    mcVariables = cms.PSet(
        probe_e = cms.string('energy'),
        probe_et = cms.string('et'),
        probe_eta = cms.string('eta'),
        probe_phi = cms.string('phi')
    ),
    motherPdgId = cms.vint32(),
    pairFlags = cms.PSet(

    ),
    pairVariables = cms.PSet(
        abseta = cms.string('abs(eta)'),
        eta = cms.string('eta'),
        mass = cms.string('mass'),
        pt = cms.string('pt')
    ),
    pfMet = cms.InputTag("slimmedMETsPuppi"),
    pileupInfoTag = cms.InputTag("slimmedAddPileupInfo"),
    probeMatches = cms.InputTag("genProbePho"),
    rho = cms.InputTag("fixedGridRhoFastjetAll"),
    tagFlags = cms.PSet(

    ),
    tagMatches = cms.InputTag("genTagEle"),
    tagProbePairs = cms.InputTag("tnpPairingPhoIDs"),
    tagVariables = cms.PSet(
        Ele_1overEminus1overP = cms.string('abs(1-eSuperClusterOverP())/ecalEnergy()'),
        Ele_3charge = cms.string('chargeInfo().isGsfCtfScPixConsistent'),
        Ele_5x5_sieie = cms.string('full5x5_showerShape().sigmaIetaIeta'),
        Ele_IsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        Ele_IsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV2Values"),
        Ele_abseta = cms.string('abs(eta)'),
        Ele_dEtaSeed = cms.string('deltaEtaSuperClusterTrackAtVtx+log(tan(superCluster.position.theta/2))-log(tan(superCluster.seed.position.theta/2))'),
        Ele_dPhiIn = cms.string('deltaPhiSuperClusterTrackAtVtx'),
        Ele_dxy = cms.InputTag("eleVarHelper","dxy"),
        Ele_dz = cms.InputTag("eleVarHelper","dz"),
        Ele_e = cms.string('energy'),
        Ele_et = cms.string('et'),
        Ele_eta = cms.string('eta'),
        Ele_hoe = cms.string('hadronicOverEm()'),
        Ele_hzzMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16HZZV1Values"),
        Ele_idCutForTrigger = cms.InputTag("eleVarHelper","idCutForTrigger"),
        Ele_ip2D = cms.InputTag("eleVarHelper","ip2D"),
        Ele_ipDZ = cms.InputTag("eleVarHelper","ipDZ"),
        Ele_isPOGIP = cms.InputTag("eleVarHelper","isPOGIP"),
        Ele_isPOGIP2D = cms.InputTag("eleVarHelper","isPOGIP2D"),
        Ele_isoCutForTrigger = cms.InputTag("eleVarHelper","isoCutForTrigger"),
        Ele_noIsoMVA94X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV1Values"),
        Ele_noIsoMVA94XV2 = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17NoIsoV2Values"),
        Ele_nonTrigMVA80X = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Spring16GeneralPurposeV1Values"),
        Ele_phi = cms.string('phi'),
        Ele_pt = cms.string('pt'),
        Ele_q = cms.string('charge'),
        Ele_relEcalIso = cms.InputTag("eleVarHelper","relEcalIso"),
        Ele_relHcalIso = cms.InputTag("eleVarHelper","relHcalIso"),
        Ele_relPFIso = cms.InputTag("eleVarHelper","relPFIso"),
        Ele_relTrkIso = cms.InputTag("eleVarHelper","relTrkIso"),
        Ele_sip = cms.InputTag("eleVarHelper","sip"),
        Ele_sip2D = cms.InputTag("eleVarHelper","sip2D"),
        Ele_trigMVA = cms.InputTag("electronMVAValueMapProducer","ElectronMVAEstimatorRun2Fall17IsoV1Values"),
        sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        sc_e = cms.string('superCluster.energy'),
        sc_et = cms.string('superCluster.energy*sin(superClusterPosition.theta)'),
        sc_eta = cms.string('-log(tan(superClusterPosition.theta/2))')
    ),
    variables = cms.PSet(
        ph_ESsigma = cms.string('full5x5_showerShapeVariables.effSigmaRR'),
        ph_abseta = cms.string('abs(eta)'),
        ph_chIso = cms.string('chargedHadronIso'),
        ph_chWorIso = cms.string('chargedHadronWorstVtxIso'),
        ph_e = cms.string('energy'),
        ph_et = cms.string('et'),
        ph_eta = cms.string('eta'),
        ph_full5x5x_r9 = cms.string('full5x5_r9'),
        ph_hoe = cms.string('hadronicOverEm'),
        ph_mva80X = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRun2Spring16NonTrigV1Values"),
        ph_mva94X = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v1p1Values"),
        ph_mva94XV2 = cms.InputTag("photonMVAValueMapProducer","PhotonMVAEstimatorRunIIFall17v2Values"),
        ph_neuIso = cms.string('neutralHadronIso'),
        ph_phoIso = cms.string('photonIso'),
        ph_preshower_energy_plane1 = cms.string('superCluster.preshowerEnergyPlane1'),
        ph_preshower_energy_plane2 = cms.string('superCluster.preshowerEnergyPlane2'),
        ph_r9 = cms.string('r9'),
        ph_s4 = cms.string('full5x5_showerShapeVariables.e2x2/full5x5_showerShapeVariables.e5x5'),
        ph_sc_abseta = cms.string('abs(-log(tan(superCluster.position.theta/2)))'),
        ph_sc_energy = cms.string('superCluster.energy'),
        ph_sc_et = cms.string('superCluster.energy*sin(superCluster.position.theta)'),
        ph_sc_eta = cms.string('-log(tan(superCluster.position.theta/2))'),
        ph_sc_etaWidth = cms.string('superCluster.etaWidth'),
        ph_sc_phiWidth = cms.string('superCluster.phiWidth'),
        ph_sc_rawEnergy = cms.string('superCluster.rawEnergy'),
        ph_sieie = cms.string('full5x5_sigmaIetaIeta'),
        ph_sieip = cms.string('full5x5_showerShapeVariables.sigmaIetaIphi')
    ),
    vertexCollection = cms.InputTag("offlineSlimmedPrimaryVertices")
)


process.DQMStore = cms.Service("DQMStore",
    LSbasedMode = cms.untracked.bool(False),
    collateHistograms = cms.untracked.bool(False),
    enableMultiThread = cms.untracked.bool(False),
    forceResetOnBeginLumi = cms.untracked.bool(False),
    referenceFileName = cms.untracked.string(''),
    saveByLumi = cms.untracked.bool(False),
    verbose = cms.untracked.int32(0),
    verboseQT = cms.untracked.int32(0)
)


process.MessageLogger = cms.Service("MessageLogger",
    FrameworkJobReport = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        optionalPSet = cms.untracked.bool(True)
    ),
    categories = cms.untracked.vstring(
        'FwkJob', 
        'FwkReport', 
        'FwkSummary', 
        'Root_NoDictionary'
    ),
    cerr = cms.untracked.PSet(
        FwkJob = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        FwkReport = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1000)
        ),
        FwkSummary = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000),
            optionalPSet = cms.untracked.bool(True),
            reportEvery = cms.untracked.int32(1)
        ),
        INFO = cms.untracked.PSet(
            limit = cms.untracked.int32(0)
        ),
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        default = cms.untracked.PSet(
            limit = cms.untracked.int32(10000000)
        ),
        noTimeStamps = cms.untracked.bool(False),
        optionalPSet = cms.untracked.bool(True),
        threshold = cms.untracked.string('')
    ),
    cerr_stats = cms.untracked.PSet(
        optionalPSet = cms.untracked.bool(True),
        output = cms.untracked.string('cerr'),
        threshold = cms.untracked.string('WARNING')
    ),
    cout = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    debugModules = cms.untracked.vstring(),
    debugs = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    default = cms.untracked.PSet(

    ),
    destinations = cms.untracked.vstring(
        'warnings', 
        'errors', 
        'infos', 
        'debugs', 
        'cout', 
        'cerr'
    ),
    errors = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    ),
    fwkJobReports = cms.untracked.vstring('FrameworkJobReport'),
    infos = cms.untracked.PSet(
        Root_NoDictionary = cms.untracked.PSet(
            limit = cms.untracked.int32(0),
            optionalPSet = cms.untracked.bool(True)
        ),
        optionalPSet = cms.untracked.bool(True),
        placeholder = cms.untracked.bool(True)
    ),
    statistics = cms.untracked.vstring('cerr_stats'),
    suppressDebug = cms.untracked.vstring(),
    suppressInfo = cms.untracked.vstring(),
    suppressWarning = cms.untracked.vstring(),
    warnings = cms.untracked.PSet(
        placeholder = cms.untracked.bool(True)
    )
)


process.RandomNumberGeneratorService = cms.Service("RandomNumberGeneratorService",
    CTPPSFastRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1357987)
    ),
    LHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    MuonSimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(987346)
    ),
    VtxSmeared = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(98765432)
    ),
    ecalPreshowerRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6541321)
    ),
    ecalRecHit = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(654321)
    ),
    externalLHEProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(234567)
    ),
    famosPileUp = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    fastSimProducer = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(13579)
    ),
    fastTrackerRecHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(24680)
    ),
    g4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    generator = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hbhereco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hfreco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    hiSignal = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(123456789)
    ),
    hiSignalG4SimHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11)
    ),
    hiSignalLHCTransport = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(88776655)
    ),
    horeco = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(541321)
    ),
    l1ParamMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(6453209)
    ),
    mix = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixData = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(12345)
    ),
    mixGenPU = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixRecoTracks = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    mixSimCaloHits = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(918273)
    ),
    paramMuons = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(54525)
    ),
    saveFileName = cms.untracked.string(''),
    simBeamSpotFilter = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(87654321)
    ),
    simMuonCSCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(11223344)
    ),
    simMuonDTDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simMuonRPCDigis = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    ),
    simSiStripDigiSimLink = cms.PSet(
        engineName = cms.untracked.string('MixMaxRng'),
        initialSeed = cms.untracked.uint32(1234567)
    )
)


process.TFileService = cms.Service("TFileService",
    closeFileFast = cms.untracked.bool(True),
    fileName = cms.string('TnPTree_mc.root')
)


process.CSCGeometryESModule = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.CaloGeometryBuilder = cms.ESProducer("CaloGeometryBuilder",
    SelectedCalos = cms.vstring(
        'HCAL', 
        'ZDC', 
        'CASTOR', 
        'EcalBarrel', 
        'EcalEndcap', 
        'EcalPreshower', 
        'TOWER'
    )
)


process.CaloTopologyBuilder = cms.ESProducer("CaloTopologyBuilder")


process.CaloTowerGeometryFromDBEP = cms.ESProducer("CaloTowerGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.CaloTowerTopologyEP = cms.ESProducer("CaloTowerTopologyEP")


process.CastorDbProducer = cms.ESProducer("CastorDbProducer",
    appendToDataLabel = cms.string('')
)


process.CastorGeometryFromDBEP = cms.ESProducer("CastorGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.DTGeometryESModule = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.EcalBarrelGeometryFromDBEP = cms.ESProducer("EcalBarrelGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalElectronicsMappingBuilder = cms.ESProducer("EcalElectronicsMappingBuilder")


process.EcalEndcapGeometryFromDBEP = cms.ESProducer("EcalEndcapGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalLaserCorrectionService = cms.ESProducer("EcalLaserCorrectionService")


process.EcalPreshowerGeometryFromDBEP = cms.ESProducer("EcalPreshowerGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.EcalTrigTowerConstituentsMapBuilder = cms.ESProducer("EcalTrigTowerConstituentsMapBuilder",
    MapFile = cms.untracked.string('Geometry/EcalMapping/data/EndCap_TTMap.txt')
)


process.GlobalTrackingGeometryESProducer = cms.ESProducer("GlobalTrackingGeometryESProducer")


process.HcalAlignmentEP = cms.ESProducer("HcalAlignmentEP")


process.HcalGeometryFromDBEP = cms.ESProducer("HcalGeometryFromDBEP",
    applyAlignment = cms.bool(True)
)


process.MuonDetLayerGeometryESProducer = cms.ESProducer("MuonDetLayerGeometryESProducer")


process.ParabolicParametrizedMagneticFieldProducer = cms.ESProducer("AutoParametrizedMagneticFieldProducer",
    label = cms.untracked.string('ParabolicMf'),
    valueOverride = cms.int32(-1),
    version = cms.string('Parabolic')
)


process.RPCGeometryESModule = cms.ESProducer("RPCGeometryESModule",
    compatibiltyWith11 = cms.untracked.bool(True),
    useDDD = cms.untracked.bool(False)
)


process.SiStripRecHitMatcherESProducer = cms.ESProducer("SiStripRecHitMatcherESProducer",
    ComponentName = cms.string('StandardMatcher'),
    NSigmaInside = cms.double(3.0),
    PreFilter = cms.bool(False)
)


process.StripCPEfromTrackAngleESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('StripCPEfromTrackAngle'),
    ComponentType = cms.string('StripCPEfromTrackAngle'),
    parameters = cms.PSet(
        mLC_P0 = cms.double(-0.326),
        mLC_P1 = cms.double(0.618),
        mLC_P2 = cms.double(0.3),
        mTEC_P0 = cms.double(-1.885),
        mTEC_P1 = cms.double(0.471),
        mTIB_P0 = cms.double(-0.742),
        mTIB_P1 = cms.double(0.202),
        mTID_P0 = cms.double(-1.427),
        mTID_P1 = cms.double(0.433),
        mTOB_P0 = cms.double(-1.026),
        mTOB_P1 = cms.double(0.253),
        maxChgOneMIP = cms.double(6000.0),
        useLegacyError = cms.bool(False)
    )
)


process.TrackerRecoGeometryESProducer = cms.ESProducer("TrackerRecoGeometryESProducer")


process.TransientTrackBuilderESProducer = cms.ESProducer("TransientTrackBuilderESProducer",
    ComponentName = cms.string('TransientTrackBuilder')
)


process.VolumeBasedMagneticFieldESProducer = cms.ESProducer("VolumeBasedMagneticFieldESProducerFromDB",
    debugBuilder = cms.untracked.bool(False),
    label = cms.untracked.string(''),
    valueOverride = cms.int32(-1)
)


process.ZdcGeometryFromDBEP = cms.ESProducer("ZdcGeometryFromDBEP",
    applyAlignment = cms.bool(False)
)


process.candidateBoostedDoubleSecondaryVertexAK8Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_AK8_BDT_v4.weights.xml.gz')
)


process.candidateBoostedDoubleSecondaryVertexCA15Computer = cms.ESProducer("CandidateBoostedDoubleSecondaryVertexESProducer",
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SecondaryVertex/data/BoostedDoubleSV_CA15_BDT_v3.weights.xml.gz')
)


process.candidateChargeBTagComputer = cms.ESProducer("CandidateChargeBTagESProducer",
    gbrForestLabel = cms.string(''),
    jetChargeExp = cms.double(0.8),
    svChargeExp = cms.double(0.5),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/ChargeBTag_4sep_2016.weights.xml.gz')
)


process.candidateCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring(
        'candidateJetProbabilityComputer', 
        'candidateJetBProbabilityComputer', 
        'candidateCombinedSecondaryVertexV2Computer', 
        'softPFMuonComputer', 
        'softPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidateCombinedSecondaryVertexSoftLeptonComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertexNoSoftLepton', 
        'CombinedSVPseudoVertexNoSoftLepton', 
        'CombinedSVNoVertexNoSoftLepton', 
        'CombinedSVRecoVertexSoftMuon', 
        'CombinedSVPseudoVertexSoftMuon', 
        'CombinedSVNoVertexSoftMuon', 
        'CombinedSVRecoVertexSoftElectron', 
        'CombinedSVPseudoVertexSoftElectron', 
        'CombinedSVNoVertexSoftElectron'
    ),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexSoftLeptonCvsLComputer = cms.ESProducer("CandidateCombinedSecondaryVertexSoftLeptonCvsLESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVRecoVertexNoSoftLeptonCvsL', 
        'CombinedSVPseudoVertexNoSoftLeptonCvsL', 
        'CombinedSVNoVertexNoSoftLeptonCvsL', 
        'CombinedSVRecoVertexSoftMuonCvsL', 
        'CombinedSVPseudoVertexSoftMuonCvsL', 
        'CombinedSVNoVertexSoftMuonCvsL', 
        'CombinedSVRecoVertexSoftElectronCvsL', 
        'CombinedSVPseudoVertexSoftElectronCvsL', 
        'CombinedSVNoVertexSoftElectronCvsL'
    ),
    categoryVariableName = cms.string('vertexLeptonCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidateGhostTrackComputer = cms.ESProducer("CandidateGhostTrackESProducer",
    calibrationRecords = cms.vstring(
        'GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    recordLabel = cms.string(''),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.candidateJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring(
        'candidateNegativeOnlyJetProbabilityComputer', 
        'candidateNegativeOnlyJetBProbabilityComputer', 
        'candidateNegativeCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidateNegativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.candidateNegativeOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D2ndComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateNegativeTrackCounting3D3rdComputer = cms.ESProducer("CandidateNegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    gbrForestLabel = cms.string('btag_CombinedMVAv2_BDT'),
    jetTagComputers = cms.vstring(
        'candidatePositiveOnlyJetProbabilityComputer', 
        'candidatePositiveOnlyJetBProbabilityComputer', 
        'candidatePositiveCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.candidatePositiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CandidateCombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.candidatePositiveOnlyJetBProbabilityComputer = cms.ESProducer("CandidateJetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidatePositiveOnlyJetProbabilityComputer = cms.ESProducer("CandidateJetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.candidateSimpleSecondaryVertex2TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateSimpleSecondaryVertex3TrkComputer = cms.ESProducer("CandidateSimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.candidateTrackCounting3D2ndComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.candidateTrackCounting3D3rdComputer = cms.ESProducer("CandidateTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.charmTagsComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_sklearn.weight.xml')
)


process.charmTagsComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_sklearn.weight.xml')
)


process.charmTagsNegativeComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(True),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(True),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(-2.0),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(True)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_sklearn.weight.xml')
)


process.charmTagsNegativeComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(True),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(True),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(-2.0),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(0),
            sip3dSigMin = cms.double(-99999.9),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(True)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_sklearn.weight.xml')
)


process.charmTagsPositiveComputerCvsB = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_b_sklearn.weight.xml')
)


process.charmTagsPositiveComputerCvsL = cms.ESProducer("CharmTaggerESProducer",
    computer = cms.ESInputTag("combinedSecondaryVertexSoftLeptonComputer"),
    defaultValueNoTracks = cms.bool(False),
    gbrForestLabel = cms.string(''),
    mvaName = cms.string('BDT'),
    slComputerCfg = cms.PSet(
        SoftLeptonFlip = cms.bool(False),
        calibrationRecords = cms.vstring(
            'CombinedSVRecoVertexNoSoftLepton', 
            'CombinedSVPseudoVertexNoSoftLepton', 
            'CombinedSVNoVertexNoSoftLepton', 
            'CombinedSVRecoVertexSoftMuon', 
            'CombinedSVPseudoVertexSoftMuon', 
            'CombinedSVNoVertexSoftMuon', 
            'CombinedSVRecoVertexSoftElectron', 
            'CombinedSVPseudoVertexSoftElectron', 
            'CombinedSVNoVertexSoftElectron'
        ),
        categoryVariableName = cms.string('vertexLeptonCategory'),
        charmCut = cms.double(1.5),
        correctVertexMass = cms.bool(False),
        minimumTrackWeight = cms.double(0.5),
        pseudoMultiplicityMin = cms.uint32(2),
        pseudoVertexV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.05)
        ),
        recordLabel = cms.string(''),
        trackFlip = cms.bool(False),
        trackMultiplicityMin = cms.uint32(2),
        trackPairV0Filter = cms.PSet(
            k0sMassWindow = cms.double(0.03)
        ),
        trackPseudoSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(2.0),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSelection = cms.PSet(
            a_dR = cms.double(-0.001053),
            a_pT = cms.double(0.005263),
            b_dR = cms.double(0.6263),
            b_pT = cms.double(0.3684),
            jetDeltaRMax = cms.double(0.3),
            maxDecayLen = cms.double(5),
            maxDistToAxis = cms.double(0.07),
            max_pT = cms.double(500),
            max_pT_dRcut = cms.double(0.1),
            max_pT_trackPTcut = cms.double(3),
            min_pT = cms.double(120),
            min_pT_dRcut = cms.double(0.5),
            normChi2Max = cms.double(99999.9),
            pixelHitsMin = cms.uint32(0),
            ptMin = cms.double(0.0),
            qualityClass = cms.string('any'),
            sip2dSigMax = cms.double(99999.9),
            sip2dSigMin = cms.double(-99999.9),
            sip2dValMax = cms.double(99999.9),
            sip2dValMin = cms.double(-99999.9),
            sip3dSigMax = cms.double(99999.9),
            sip3dSigMin = cms.double(0),
            sip3dValMax = cms.double(99999.9),
            sip3dValMin = cms.double(-99999.9),
            totalHitsMin = cms.uint32(0),
            useVariableJTA = cms.bool(False)
        ),
        trackSort = cms.string('sip2dSig'),
        useCategories = cms.bool(True),
        useTrackWeights = cms.bool(True),
        vertexFlip = cms.bool(False)
    ),
    tagInfos = cms.VInputTag(cms.InputTag("pfImpactParameterTagInfos"), cms.InputTag("pfInclusiveSecondaryVertexFinderCvsLTagInfos"), cms.InputTag("softPFMuonsTagInfos"), cms.InputTag("softPFElectronsTagInfos")),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.VPSet(
        cms.PSet(
            default = cms.double(-1),
            name = cms.string('vertexLeptonCategory'),
            taggingVarName = cms.string('vertexLeptonCategory')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSig_0'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip2dSig_1'),
            taggingVarName = cms.string('trackSip2dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSig_0'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-100),
            idx = cms.int32(1),
            name = cms.string('trackSip3dSig_1'),
            taggingVarName = cms.string('trackSip3dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPtRel_0'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPtRel_1'),
            taggingVarName = cms.string('trackPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackPPar_0'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackPPar_1'),
            taggingVarName = cms.string('trackPPar')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('trackEtaRel_0'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('trackEtaRel_1'),
            taggingVarName = cms.string('trackEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDeltaR_0'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDeltaR_1'),
            taggingVarName = cms.string('trackDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackPtRatio_0'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackPtRatio_1'),
            taggingVarName = cms.string('trackPtRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(0),
            name = cms.string('trackPParRatio_0'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(1.1),
            idx = cms.int32(1),
            name = cms.string('trackPParRatio_1'),
            taggingVarName = cms.string('trackPParRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackJetDist_0'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackJetDist_1'),
            taggingVarName = cms.string('trackJetDist')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('trackDecayLenVal_0'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(1),
            name = cms.string('trackDecayLenVal_1'),
            taggingVarName = cms.string('trackDecayLenVal')
        ), 
        cms.PSet(
            default = cms.double(0),
            name = cms.string('jetNSecondaryVertices'),
            taggingVarName = cms.string('jetNSecondaryVertices')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('jetNTracks'),
            taggingVarName = cms.string('jetNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetEtRatio'),
            taggingVarName = cms.string('trackSumJetEtRatio')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            name = cms.string('trackSumJetDeltaR'),
            taggingVarName = cms.string('trackSumJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexMass_0'),
            taggingVarName = cms.string('vertexMass')
        ), 
        cms.PSet(
            default = cms.double(-10),
            idx = cms.int32(0),
            name = cms.string('vertexEnergyRatio_0'),
            taggingVarName = cms.string('vertexEnergyRatio')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip2dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip2dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-999),
            idx = cms.int32(0),
            name = cms.string('trackSip3dSigAboveCharm_0'),
            taggingVarName = cms.string('trackSip3dSigAboveCharm')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance2dSig_0'),
            taggingVarName = cms.string('flightDistance2dSig')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('flightDistance3dSig_0'),
            taggingVarName = cms.string('flightDistance3dSig')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexJetDeltaR_0'),
            taggingVarName = cms.string('vertexJetDeltaR')
        ), 
        cms.PSet(
            default = cms.double(0),
            idx = cms.int32(0),
            name = cms.string('vertexNTracks_0'),
            taggingVarName = cms.string('vertexNTracks')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('massVertexEnergyFraction_0'),
            taggingVarName = cms.string('massVertexEnergyFraction')
        ), 
        cms.PSet(
            default = cms.double(-0.1),
            idx = cms.int32(0),
            name = cms.string('vertexBoostOverSqrtJetPt_0'),
            taggingVarName = cms.string('vertexBoostOverSqrtJetPt')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonPtRel_0'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonPtRel_1'),
            taggingVarName = cms.string('leptonPtRel')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(0),
            name = cms.string('leptonSip3d_0'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-10000),
            idx = cms.int32(1),
            name = cms.string('leptonSip3d_1'),
            taggingVarName = cms.string('leptonSip3d')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonDeltaR_0'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonDeltaR_1'),
            taggingVarName = cms.string('leptonDeltaR')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatioRel_0'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatioRel_1'),
            taggingVarName = cms.string('leptonRatioRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonEtaRel_0'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonEtaRel_1'),
            taggingVarName = cms.string('leptonEtaRel')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(0),
            name = cms.string('leptonRatio_0'),
            taggingVarName = cms.string('leptonRatio')
        ), 
        cms.PSet(
            default = cms.double(-1),
            idx = cms.int32(1),
            name = cms.string('leptonRatio_1'),
            taggingVarName = cms.string('leptonRatio')
        )
    ),
    weightFile = cms.FileInPath('RecoBTag/CTagging/data/c_vs_udsg_sklearn.weight.xml')
)


process.combinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring(
        'jetProbabilityComputer', 
        'jetBProbabilityComputer', 
        'combinedSecondaryVertexV2Computer', 
        'softPFMuonComputer', 
        'softPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.combinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.doubleVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    minVertices = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.fakeForIdealAlignment = cms.ESProducer("FakeAlignmentProducer",
    appendToDataLabel = cms.string('fakeForIdeal')
)


process.ghostTrackComputer = cms.ESProducer("GhostTrackESProducer",
    calibrationRecords = cms.vstring(
        'GhostTrackRecoVertex', 
        'GhostTrackPseudoVertex', 
        'GhostTrackNoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    minimumTrackWeight = cms.double(0.5),
    recordLabel = cms.string(''),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True)
)


process.hcalDDDRecConstants = cms.ESProducer("HcalDDDRecConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalDDDSimConstants = cms.ESProducer("HcalDDDSimConstantsESModule",
    appendToDataLabel = cms.string('')
)


process.hcalTopologyIdeal = cms.ESProducer("HcalTopologyIdealEP",
    Exclude = cms.untracked.string(''),
    MergePosition = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
)


process.hcal_db_producer = cms.ESProducer("HcalDbProducer",
    dump = cms.untracked.vstring(''),
    file = cms.untracked.string('')
)


process.idealForDigiCSCGeometry = cms.ESProducer("CSCGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    debugV = cms.untracked.bool(False),
    useCentreTIOffsets = cms.bool(False),
    useDDD = cms.bool(False),
    useGangedStripsInME1a = cms.bool(True),
    useOnlyWiresInME1a = cms.bool(False),
    useRealWireGeometry = cms.bool(True)
)


process.idealForDigiDTGeometry = cms.ESProducer("DTGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.idealForDigiTrackerGeometry = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string('fakeForIdeal'),
    appendToDataLabel = cms.string('idealForDigi'),
    applyAlignment = cms.bool(False),
    fromDDD = cms.bool(False)
)


process.impactParameterMVAComputer = cms.ESProducer("GenericMVAJetTagESProducer",
    calibrationRecord = cms.string('ImpactParameterMVA'),
    recordLabel = cms.string(''),
    useCategories = cms.bool(False)
)


process.jetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.jetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring(
        'negativeOnlyJetProbabilityComputer', 
        'negativeOnlyJetBProbabilityComputer', 
        'negativeCombinedSecondaryVertexV2Computer', 
        'negativeSoftPFMuonComputer', 
        'negativeSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.negativeCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(True),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(-2.0),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(0),
        sip3dSigMin = cms.double(-99999.9),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(True)
)


process.negativeOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(-1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.negativeSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.negativeSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(False)
)


process.negativeSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('negative'),
    use3d = cms.bool(True)
)


process.negativeSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('negative')
)


process.negativeSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('negative'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.negativeTrackCounting3D2ndComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.negativeTrackCounting3D3rdComputer = cms.ESProducer("NegativeTrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.positiveCombinedMVAV2Computer = cms.ESProducer("CombinedMVAV2JetTagESProducer",
    jetTagComputers = cms.vstring(
        'positiveOnlyJetProbabilityComputer', 
        'positiveOnlyJetBProbabilityComputer', 
        'positiveCombinedSecondaryVertexV2Computer', 
        'positiveSoftPFMuonComputer', 
        'positiveSoftPFElectronComputer'
    ),
    mvaName = cms.string('bdt'),
    spectators = cms.vstring(),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(False),
    useGBRForest = cms.bool(True),
    variables = cms.vstring(
        'Jet_CSV', 
        'Jet_CSVIVF', 
        'Jet_JP', 
        'Jet_JBP', 
        'Jet_SoftMu', 
        'Jet_SoftEl'
    ),
    weightFile = cms.FileInPath('RecoBTag/Combined/data/CombinedMVAV2_13_07_2015.weights.xml.gz')
)


process.positiveCombinedSecondaryVertexV2Computer = cms.ESProducer("CombinedSecondaryVertexESProducer",
    SoftLeptonFlip = cms.bool(False),
    calibrationRecords = cms.vstring(
        'CombinedSVIVFV2RecoVertex', 
        'CombinedSVIVFV2PseudoVertex', 
        'CombinedSVIVFV2NoVertex'
    ),
    categoryVariableName = cms.string('vertexCategory'),
    charmCut = cms.double(1.5),
    correctVertexMass = cms.bool(True),
    minimumTrackWeight = cms.double(0.5),
    pseudoMultiplicityMin = cms.uint32(2),
    pseudoVertexV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
    ),
    recordLabel = cms.string(''),
    trackFlip = cms.bool(False),
    trackMultiplicityMin = cms.uint32(2),
    trackPairV0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.03)
    ),
    trackPseudoSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(2.0),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSelection = cms.PSet(
        a_dR = cms.double(-0.001053),
        a_pT = cms.double(0.005263),
        b_dR = cms.double(0.6263),
        b_pT = cms.double(0.3684),
        jetDeltaRMax = cms.double(0.3),
        maxDecayLen = cms.double(5),
        maxDistToAxis = cms.double(0.07),
        max_pT = cms.double(500),
        max_pT_dRcut = cms.double(0.1),
        max_pT_trackPTcut = cms.double(3),
        min_pT = cms.double(120),
        min_pT_dRcut = cms.double(0.5),
        normChi2Max = cms.double(99999.9),
        pixelHitsMin = cms.uint32(0),
        ptMin = cms.double(0.0),
        qualityClass = cms.string('any'),
        sip2dSigMax = cms.double(99999.9),
        sip2dSigMin = cms.double(-99999.9),
        sip2dValMax = cms.double(99999.9),
        sip2dValMin = cms.double(-99999.9),
        sip3dSigMax = cms.double(99999.9),
        sip3dSigMin = cms.double(0),
        sip3dValMax = cms.double(99999.9),
        sip3dValMin = cms.double(-99999.9),
        totalHitsMin = cms.uint32(0),
        useVariableJTA = cms.bool(False)
    ),
    trackSort = cms.string('sip2dSig'),
    useCategories = cms.bool(True),
    useTrackWeights = cms.bool(True),
    vertexFlip = cms.bool(False)
)


process.positiveOnlyJetBProbabilityComputer = cms.ESProducer("JetBProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    numberOfBTracks = cms.uint32(4),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveOnlyJetProbabilityComputer = cms.ESProducer("JetProbabilityESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(0.3),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumProbability = cms.double(0.005),
    trackIpSign = cms.int32(1),
    trackQualityClass = cms.string('any'),
    useVariableJTA = cms.bool(False)
)


process.positiveSoftPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.positiveSoftPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(False)
)


process.positiveSoftPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('positive'),
    use3d = cms.bool(True)
)


process.positiveSoftPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('positive')
)


process.positiveSoftPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('positive'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.siPixelQualityESProducer = cms.ESProducer("SiPixelQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiPixelQualityFromDbRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiPixelDetVOffRcd'),
            tag = cms.string('')
        )
    ),
    siPixelQualityLabel = cms.string('')
)


process.siStripBackPlaneCorrectionDepESProducer = cms.ESProducer("SiStripBackPlaneCorrectionDepESProducer",
    BackPlaneCorrectionDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    BackPlaneCorrectionPeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripBackPlaneCorrectionRcd')
    ),
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    )
)


process.siStripGainESProducer = cms.ESProducer("SiStripGainESProducer",
    APVGain = cms.VPSet(
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGainRcd')
        ), 
        cms.PSet(
            Label = cms.untracked.string(''),
            NormalizationFactor = cms.untracked.double(1.0),
            Record = cms.string('SiStripApvGain2Rcd')
        )
    ),
    AutomaticNormalization = cms.bool(False),
    appendToDataLabel = cms.string(''),
    printDebug = cms.untracked.bool(False)
)


process.siStripLorentzAngleDepESProducer = cms.ESProducer("SiStripLorentzAngleDepESProducer",
    LatencyRecord = cms.PSet(
        label = cms.untracked.string(''),
        record = cms.string('SiStripLatencyRcd')
    ),
    LorentzAngleDeconvMode = cms.PSet(
        label = cms.untracked.string('deconvolution'),
        record = cms.string('SiStripLorentzAngleRcd')
    ),
    LorentzAnglePeakMode = cms.PSet(
        label = cms.untracked.string('peak'),
        record = cms.string('SiStripLorentzAngleRcd')
    )
)


process.siStripQualityESProducer = cms.ESProducer("SiStripQualityESProducer",
    ListOfRecordToMerge = cms.VPSet(
        cms.PSet(
            record = cms.string('SiStripDetVOffRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripDetCablingRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('RunInfoRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadChannelRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadFiberRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadModuleRcd'),
            tag = cms.string('')
        ), 
        cms.PSet(
            record = cms.string('SiStripBadStripRcd'),
            tag = cms.string('')
        )
    ),
    PrintDebugOutput = cms.bool(False),
    ReduceGranularity = cms.bool(False),
    ThresholdForReducedGranularity = cms.double(0.3),
    UseEmptyRunInfo = cms.bool(False),
    appendToDataLabel = cms.string('')
)


process.simpleSecondaryVertex2TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(2),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.simpleSecondaryVertex3TrkComputer = cms.ESProducer("SimpleSecondaryVertexESProducer",
    minTracks = cms.uint32(3),
    unBoost = cms.bool(False),
    use3d = cms.bool(True),
    useSignificance = cms.bool(True)
)


process.sistripconn = cms.ESProducer("SiStripConnectivity")


process.softPFElectronByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFElectronByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFElectronByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFElectronComputer = cms.ESProducer("ElectronTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFElectron_BDT'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(False),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFElectron_BDT.weights.xml.gz')
)


process.softPFMuonByIP2dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(False)
)


process.softPFMuonByIP3dComputer = cms.ESProducer("LeptonTaggerByIPESProducer",
    ipSign = cms.string('any'),
    use3d = cms.bool(True)
)


process.softPFMuonByPtComputer = cms.ESProducer("LeptonTaggerByPtESProducer",
    ipSign = cms.string('any')
)


process.softPFMuonComputer = cms.ESProducer("MuonTaggerESProducer",
    gbrForestLabel = cms.string('btag_SoftPFMuon_BDT'),
    ipSign = cms.string('any'),
    useAdaBoost = cms.bool(True),
    useCondDB = cms.bool(True),
    useGBRForest = cms.bool(True),
    weightFile = cms.FileInPath('RecoBTag/SoftLepton/data/SoftPFMuon_BDT.weights.xml.gz')
)


process.stripCPEESProducer = cms.ESProducer("StripCPEESProducer",
    ComponentName = cms.string('stripCPE'),
    ComponentType = cms.string('SimpleStripCPE'),
    parameters = cms.PSet(

    )
)


process.trackCounting3D2ndComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(2),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackCounting3D3rdComputer = cms.ESProducer("TrackCountingESProducer",
    a_dR = cms.double(-0.001053),
    a_pT = cms.double(0.005263),
    b_dR = cms.double(0.6263),
    b_pT = cms.double(0.3684),
    deltaR = cms.double(-1.0),
    impactParameterType = cms.int32(0),
    max_pT = cms.double(500),
    max_pT_dRcut = cms.double(0.1),
    max_pT_trackPTcut = cms.double(3),
    maximumDecayLength = cms.double(5.0),
    maximumDistanceToJetAxis = cms.double(0.07),
    min_pT = cms.double(120),
    min_pT_dRcut = cms.double(0.5),
    minimumImpactParameter = cms.double(-1),
    nthTrack = cms.int32(3),
    trackQualityClass = cms.string('any'),
    useSignedImpactParameterSig = cms.bool(True),
    useVariableJTA = cms.bool(False)
)


process.trackerGeometryDB = cms.ESProducer("TrackerDigiGeometryESModule",
    alignmentsLabel = cms.string(''),
    appendToDataLabel = cms.string(''),
    applyAlignment = cms.bool(True),
    fromDDD = cms.bool(False)
)


process.trackerNumberingGeometryDB = cms.ESProducer("TrackerGeometricDetESModule",
    appendToDataLabel = cms.string(''),
    fromDDD = cms.bool(False)
)


process.trackerTopology = cms.ESProducer("TrackerTopologyEP",
    appendToDataLabel = cms.string('')
)


process.BTagRecord = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('JetTagComputerRecord')
)


process.GlobalTag = cms.ESSource("PoolDBESSource",
    DBParameters = cms.PSet(
        authenticationPath = cms.untracked.string(''),
        authenticationSystem = cms.untracked.int32(0),
        messageLevel = cms.untracked.int32(0),
        security = cms.untracked.string('')
    ),
    DumpStat = cms.untracked.bool(False),
    ReconnectEachRun = cms.untracked.bool(False),
    RefreshAlways = cms.untracked.bool(False),
    RefreshEachRun = cms.untracked.bool(False),
    RefreshOpenIOVs = cms.untracked.bool(False),
    connect = cms.string('frontier://FrontierProd/CMS_CONDITIONS'),
    globaltag = cms.string('106X_dataRun2_v28'),
    pfnPostfix = cms.untracked.string(''),
    pfnPrefix = cms.untracked.string(''),
    snapshotTime = cms.string(''),
    toGet = cms.VPSet()
)


process.HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string('HBHE'),
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(
            slope = cms.double(-3.178648),
            tmax = cms.double(16.0),
            tzero = cms.double(23.960177)
        ), 
        cms.PSet(
            slope = cms.double(-1.5610227),
            tmax = cms.double(10.0),
            tzero = cms.double(11.977461)
        ), 
        cms.PSet(
            slope = cms.double(-1.075824),
            tmax = cms.double(6.25),
            tzero = cms.double(9.109694)
        )
    ),
    timeSlewParametersM3 = cms.VPSet(
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(15.5),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-3.2),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(32.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        ), 
        cms.PSet(
            cap = cms.double(6.0),
            tspar0 = cms.double(12.2999),
            tspar0_siPM = cms.double(0.0),
            tspar1 = cms.double(-2.19142),
            tspar1_siPM = cms.double(0.0),
            tspar2 = cms.double(0.0),
            tspar2_siPM = cms.double(0.0)
        )
    )
)


process.HepPDTESSource = cms.ESSource("HepPDTESSource",
    pdtFileName = cms.FileInPath('SimGeneral/HepPDTESSource/data/pythiaparticle.tbl')
)


process.eegeom = cms.ESSource("EmptyESSource",
    firstValid = cms.vuint32(1),
    iovIsRunNotTime = cms.bool(True),
    recordName = cms.string('EcalMappingRcd')
)


process.es_hardcode = cms.ESSource("HcalHardcodeCalibrations",
    GainWidthsForTrigPrims = cms.bool(False),
    HBRecalibration = cms.bool(False),
    HBmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHB.txt'),
    HBreCalibCutoff = cms.double(20.0),
    HERecalibration = cms.bool(False),
    HEmeanenergies = cms.FileInPath('CalibCalorimetry/HcalPlugins/data/meanenergiesHE.txt'),
    HEreCalibCutoff = cms.double(20.0),
    HFRecalParameterBlock = cms.PSet(
        HFdepthOneParameterA = cms.vdouble(
            0.004123, 0.00602, 0.008201, 0.010489, 0.013379, 
            0.016997, 0.021464, 0.027371, 0.034195, 0.044807, 
            0.058939, 0.125497
        ),
        HFdepthOneParameterB = cms.vdouble(
            -4e-06, -2e-06, 0.0, 4e-06, 1.5e-05, 
            2.6e-05, 6.3e-05, 8.4e-05, 0.00016, 0.000107, 
            0.000425, 0.000209
        ),
        HFdepthTwoParameterA = cms.vdouble(
            0.002861, 0.004168, 0.0064, 0.008388, 0.011601, 
            0.014425, 0.018633, 0.023232, 0.028274, 0.035447, 
            0.051579, 0.086593
        ),
        HFdepthTwoParameterB = cms.vdouble(
            -2e-06, -0.0, -7e-06, -6e-06, -2e-06, 
            1e-06, 1.9e-05, 3.1e-05, 6.7e-05, 1.2e-05, 
            0.000157, -3e-06
        )
    ),
    HFRecalibration = cms.bool(False),
    SiPMCharacteristics = cms.VPSet(
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(36000)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(2500)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.17),
            nonlin1 = cms.double(1.00985),
            nonlin2 = cms.double(7.84089e-06),
            nonlin3 = cms.double(2.86282e-10),
            pixels = cms.int32(27370)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.196),
            nonlin1 = cms.double(1.00546),
            nonlin2 = cms.double(6.40239e-06),
            nonlin3 = cms.double(1.27011e-10),
            pixels = cms.int32(38018)
        ), 
        cms.PSet(
            crosstalk = cms.double(0.0),
            nonlin1 = cms.double(1.0),
            nonlin2 = cms.double(0.0),
            nonlin3 = cms.double(0.0),
            pixels = cms.int32(0)
        )
    ),
    hb = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.19),
        gainWidth = cms.vdouble(0.0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.285),
        pedestalWidth = cms.double(0.809),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.49, 1.8, 7.2, 37.9),
        qieSlope = cms.vdouble(0.912, 0.917, 0.922, 0.923),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(8)
    ),
    hbUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(150),
            intlumiToNeutrons = cms.double(367000000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(-5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    he = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.23),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(125),
        pedestal = cms.double(3.163),
        pedestalWidth = cms.double(0.9698),
        photoelectronsToAnalog = cms.double(0.3305),
        qieOffset = cms.vdouble(-0.38, 2.0, 7.6, 39.6),
        qieSlope = cms.vdouble(0.912, 0.916, 0.92, 0.922),
        qieType = cms.int32(0),
        recoShape = cms.int32(105),
        zsThreshold = cms.int32(9)
    ),
    heUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.01, 0.015),
        doRadiationDamage = cms.bool(True),
        gain = cms.vdouble(0.0006252),
        gainWidth = cms.vdouble(0),
        mcShape = cms.int32(206),
        pedestal = cms.double(17.3),
        pedestalWidth = cms.double(1.5),
        photoelectronsToAnalog = cms.double(40.0),
        qieOffset = cms.vdouble(0.0, 0.0, 0.0, 0.0),
        qieSlope = cms.vdouble(0.05376, 0.05376, 0.05376, 0.05376),
        qieType = cms.int32(2),
        radiationDamage = cms.PSet(
            depVsNeutrons = cms.vdouble(5.543e-10, 8.012e-10),
            depVsTemp = cms.double(0.0631),
            intlumiOffset = cms.double(75),
            intlumiToNeutrons = cms.double(29200000.0),
            temperatureBase = cms.double(20),
            temperatureNew = cms.double(5)
        ),
        recoShape = cms.int32(206),
        zsThreshold = cms.int32(16)
    ),
    hf = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(9.354),
        pedestalWidth = cms.double(2.516),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(-0.87, 1.4, 7.8, -29.6),
        qieSlope = cms.vdouble(0.359, 0.358, 0.36, 0.367),
        qieType = cms.int32(0),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    hfUpgrade = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.14, 0.135),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(301),
        pedestal = cms.double(13.33),
        pedestalWidth = cms.double(3.33),
        photoelectronsToAnalog = cms.double(0.0),
        qieOffset = cms.vdouble(0.0697, -0.7405, 12.38, -671.9),
        qieSlope = cms.vdouble(0.297, 0.298, 0.298, 0.313),
        qieType = cms.int32(1),
        recoShape = cms.int32(301),
        zsThreshold = cms.int32(-9999)
    ),
    ho = cms.PSet(
        darkCurrent = cms.vdouble(0.0),
        doRadiationDamage = cms.bool(False),
        gain = cms.vdouble(0.006, 0.0087),
        gainWidth = cms.vdouble(0.0, 0.0),
        mcShape = cms.int32(201),
        pedestal = cms.double(12.06),
        pedestalWidth = cms.double(0.6285),
        photoelectronsToAnalog = cms.double(4.0),
        qieOffset = cms.vdouble(-0.44, 1.4, 7.1, 38.5),
        qieSlope = cms.vdouble(0.907, 0.915, 0.92, 0.921),
        qieType = cms.int32(0),
        recoShape = cms.int32(201),
        zsThreshold = cms.int32(24)
    ),
    iLumi = cms.double(-1.0),
    killHE = cms.bool(False),
    testHEPlan1 = cms.bool(False),
    testHFQIE10 = cms.bool(False),
    toGet = cms.untracked.vstring('GainWidths'),
    useHBUpgrade = cms.bool(False),
    useHEUpgrade = cms.bool(False),
    useHFUpgrade = cms.bool(False),
    useHOUpgrade = cms.bool(True),
    useIeta18depth1 = cms.bool(True),
    useLayer0Weight = cms.bool(False)
)


process.prefer("es_hardcode")

process.egmPhotonIDTask = cms.Task(process.egmPhotonIDs, process.photonMVAValueMapProducer)


process.patAlgosToolsTask = cms.Task(process.patJetCorrFactorsTransientCorrectedUpdated, process.patJetCorrFactorsUpdated, process.pfDeepCSVTagInfosUpdated, process.pfDeepFlavourJetTagsUpdated, process.pfDeepFlavourTagInfosUpdated, process.pfImpactParameterTagInfosUpdated, process.pfInclusiveSecondaryVertexFinderTagInfosUpdated, process.selectedUpdatedPatJetsUpdated, process.updatedPatJetsTransientCorrectedUpdated, process.updatedPatJetsUpdated)


process.egmGsfElectronIDTask = cms.Task(process.egmGsfElectronIDs, process.electronMVAValueMapProducer)


process.tnpPairs_sequence = cms.Sequence(process.tnpPairingEleHLT+process.tnpPairingEleIDs)


process.sc_sequenceMiniAOD = cms.Sequence(process.superClusterCands+process.goodSuperClusters)


process.ele_sequence = cms.Sequence(process.probeEleHLTsafe+process.probeEleDoubleEleHLTsafe+process.probeEleCutBasedVeto80X+process.probeEleCutBasedVeto94X+process.probeEleCutBasedVeto94XV2+process.probeEleCutBasedLoose80X+process.probeEleCutBasedLoose94X+process.probeEleCutBasedLoose94XV2+process.probeEleCutBasedMedium80X+process.probeEleCutBasedMedium94X+process.probeEleCutBasedMedium94XV2+process.probeEleCutBasedTight80X+process.probeEleCutBasedTight94X+process.probeEleCutBasedTight94XV2+process.probeEleMVA80Xwp80+process.probeEleMVA80Xwp90+process.probeEleMVA94Xwp80noiso+process.probeEleMVA94Xwp80iso+process.probeEleMVA94Xwp80noisoV2+process.probeEleMVA94Xwp80isoV2+process.probeEleMVA94Xwp90noiso+process.probeEleMVA94Xwp90iso+process.probeEleMVA94Xwp90noisoV2+process.probeEleMVA94Xwp90isoV2+process.probeEleMVA94XwpLoosenoiso+process.probeEleMVA94XwpLooseiso+process.probeEleMVA94XwpLoosenoisoV2+process.probeEleMVA94XwpLooseisoV2+process.probeEleMVA94XwpHZZisoV2+process.probeEleCutBasedVeto94XV2MinPtCut+process.probeEleCutBasedLoose94XV2MinPtCut+process.probeEleCutBasedMedium94XV2MinPtCut+process.probeEleCutBasedTight94XV2MinPtCut+process.probeEleCutBasedVeto94XV2GsfEleSCEtaMultiRangeCut+process.probeEleCutBasedLoose94XV2GsfEleSCEtaMultiRangeCut+process.probeEleCutBasedMedium94XV2GsfEleSCEtaMultiRangeCut+process.probeEleCutBasedTight94XV2GsfEleSCEtaMultiRangeCut+process.probeEleCutBasedVeto94XV2GsfEleDEtaInSeedCut+process.probeEleCutBasedLoose94XV2GsfEleDEtaInSeedCut+process.probeEleCutBasedMedium94XV2GsfEleDEtaInSeedCut+process.probeEleCutBasedTight94XV2GsfEleDEtaInSeedCut+process.probeEleCutBasedVeto94XV2GsfEleDPhiInCut+process.probeEleCutBasedLoose94XV2GsfEleDPhiInCut+process.probeEleCutBasedMedium94XV2GsfEleDPhiInCut+process.probeEleCutBasedTight94XV2GsfEleDPhiInCut+process.probeEleCutBasedVeto94XV2GsfEleFull5x5SigmaIEtaIEtaCut+process.probeEleCutBasedLoose94XV2GsfEleFull5x5SigmaIEtaIEtaCut+process.probeEleCutBasedMedium94XV2GsfEleFull5x5SigmaIEtaIEtaCut+process.probeEleCutBasedTight94XV2GsfEleFull5x5SigmaIEtaIEtaCut+process.probeEleCutBasedVeto94XV2GsfEleHadronicOverEMEnergyScaledCut+process.probeEleCutBasedLoose94XV2GsfEleHadronicOverEMEnergyScaledCut+process.probeEleCutBasedMedium94XV2GsfEleHadronicOverEMEnergyScaledCut+process.probeEleCutBasedTight94XV2GsfEleHadronicOverEMEnergyScaledCut+process.probeEleCutBasedVeto94XV2GsfEleEInverseMinusPInverseCut+process.probeEleCutBasedLoose94XV2GsfEleEInverseMinusPInverseCut+process.probeEleCutBasedMedium94XV2GsfEleEInverseMinusPInverseCut+process.probeEleCutBasedTight94XV2GsfEleEInverseMinusPInverseCut+process.probeEleCutBasedVeto94XV2GsfEleRelPFIsoScaledCut+process.probeEleCutBasedLoose94XV2GsfEleRelPFIsoScaledCut+process.probeEleCutBasedMedium94XV2GsfEleRelPFIsoScaledCut+process.probeEleCutBasedTight94XV2GsfEleRelPFIsoScaledCut+process.probeEleCutBasedVeto94XV2GsfEleConversionVetoCut+process.probeEleCutBasedLoose94XV2GsfEleConversionVetoCut+process.probeEleCutBasedMedium94XV2GsfEleConversionVetoCut+process.probeEleCutBasedTight94XV2GsfEleConversionVetoCut+process.probeEleCutBasedVeto94XV2GsfEleMissingHitsCut+process.probeEleCutBasedLoose94XV2GsfEleMissingHitsCut+process.probeEleCutBasedMedium94XV2GsfEleMissingHitsCut+process.probeEleCutBasedTight94XV2GsfEleMissingHitsCut+(process.probeEle)+process.goodElectronProbesL1+process.probeEleL1matched+process.genProbeEle)


process.tag_sequence = cms.Sequence(process.goodElectrons+process.tagEleCutBasedTight+process.tagEle+process.genEle+process.genTagEle)


process.sc_sequence = cms.Sequence(process.sc_sequenceMiniAOD+process.probeSC+process.probeSCEle+process.genProbeSC)


process.mc_sequence = cms.Sequence(process.pileupReweightingProducer)


process.hlt_sequence = cms.Sequence(process.hltFilter+process.passHltDoubleEle33CaloIdLMWSeedLegL1match+process.passHltEle32DoubleEGWPTightGsf+process.passEGL1SingleEGOr+process.passHltDoubleEle33CaloIdLMWUnsLeg+process.passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg2+process.passHltEle23Ele12CaloIdLTrackIdLIsoVLLeg1L1match)


process.tree_sequence = cms.Sequence(process.tnpEleTrig+process.tnpEleIDs)


process.pho_sequence = cms.Sequence(process.goodPhotons+(process.probePhoCutBasedLoose80X+process.probePhoCutBasedLoose94X+process.probePhoCutBasedLoose94XV2+process.probePhoCutBasedMedium80X+process.probePhoCutBasedMedium94X+process.probePhoCutBasedMedium94XV2+process.probePhoCutBasedTight80X+process.probePhoCutBasedTight94X+process.probePhoCutBasedTight94XV2+process.probePhoMVA80Xwp80+process.probePhoMVA94XV2wp80+process.probePhoMVA80Xwp90+process.probePhoMVA94XV2wp90+process.probePhoCutBasedLoose94XV2MinPtCut+process.probePhoCutBasedMedium94XV2MinPtCut+process.probePhoCutBasedTight94XV2MinPtCut+process.probePhoCutBasedLoose94XV2PhoSCEtaMultiRangeCut+process.probePhoCutBasedMedium94XV2PhoSCEtaMultiRangeCut+process.probePhoCutBasedTight94XV2PhoSCEtaMultiRangeCut+process.probePhoCutBasedLoose94XV2PhoSingleTowerHadOverEmCut+process.probePhoCutBasedMedium94XV2PhoSingleTowerHadOverEmCut+process.probePhoCutBasedTight94XV2PhoSingleTowerHadOverEmCut+process.probePhoCutBasedLoose94XV2PhoFull5x5SigmaIEtaIEtaCut+process.probePhoCutBasedMedium94XV2PhoFull5x5SigmaIEtaIEtaCut+process.probePhoCutBasedTight94XV2PhoFull5x5SigmaIEtaIEtaCut+process.probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut+process.probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut+process.probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut+process.probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut1+process.probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut1+process.probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut1+process.probePhoCutBasedLoose94XV2PhoGenericRhoPtScaledCut2+process.probePhoCutBasedMedium94XV2PhoGenericRhoPtScaledCut2+process.probePhoCutBasedTight94XV2PhoGenericRhoPtScaledCut2)+(process.probePho)+process.genProbePho)


process.egmPhotonIDSequence = cms.Sequence(process.egmPhotonIDTask)


process.egmGsfElectronIDSequence = cms.Sequence(process.egmGsfElectronIDTask)


process.init_sequence = cms.Sequence(process.egmGsfElectronIDSequence+process.egmPhotonIDSequence+process.eleVarHelper+cms.Sequence((process.ptRatioRelForEle)+(process.isoForEleFall17)+(process.isoForEleSummer16)+(process.isoForEleSpring15)+(process.leptonMvaTTH+process.leptonMvaGhent+process.leptonMvaTOP), process.patAlgosToolsTask))


process.cand_sequence = cms.Sequence(process.init_sequence+process.tag_sequence+process.ele_sequence+process.hlt_sequence)


process.p = cms.Path(process.evtCounter+process.hltFilter+process.cand_sequence+process.tnpPairs_sequence+process.mc_sequence+process.tree_sequence)


