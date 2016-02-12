# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: TTbar_8TeV_TuneCUETP8M1_cfi --conditions auto:run1_mc -n 10 --eventcontent RAWSIM --relval 9000,100 -s GEN,SIM --datatier GEN-SIM --beamspot Realistic8TeVCollision --io ProdTTbar.io --python ProdTTbar.py --fileout file:step1.root
import FWCore.ParameterSet.Config as cms

process = cms.Process('SIM')

# import of standard configurations
#   load config for step1  (gen step)
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.Geometry.GeometrySimDB_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic8TeVCollision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('Configuration.StandardSequences.SimIdeal_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_condDBv2_cff')
# load additional config for step2 (digi step)
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.SimL1Emulator_cff')
process.load('Configuration.StandardSequences.DigiToRaw_cff')
process.load('HLTrigger.Configuration.HLT_Fake_cff')
process.load('Configuration.StandardSequences.RawToDigi_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load("Configuration.StandardSequences.SimulationRandomNumberGeneratorSeeds_cff")
process.MessageLogger.cerr.FwkReport.reportEvery = 1

process.RandomNumberGeneratorService.generator.initialSeed = 345678912
# process.RandomNumberGeneratorService.g4SimHits.initialSeed = 012345678
# process.RandomNumberGeneratorService.VtxSmeared.initialSeed = 123456789
# process.rndmStore = cms.EDProducer("RandomEngineStateProducer")


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('TTbar_8TeV_TuneCUETP8M1_cfi nevts:10'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.RAWSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('GEN-SIM-RAW'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(5242880),
    fileName = cms.untracked.string('file:RAW_Zprime_8_norad.root'),
    outputCommands = process.RAWSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
from Configuration.AlCa.GlobalTag_condDBv2 import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:run1_mc', '')

# process.generator = cms.EDFilter("Pythia8GeneratorFilter",
#    PythiaParameters = cms.PSet(
#        parameterSets = cms.vstring('pythia8CommonSettings', 
#            'pythia8CUEP8M1Settings', 
#            'processParameters'),
#        processParameters = cms.vstring('Top:gg2ttbar = on ', 
#            'Top:gg2ttbar = on ', 
#            '6:m0 = 175 '),
#        pythia8CUEP8M1Settings = cms.vstring('Tune:pp 14', 
#            'Tune:ee 7', 
#            'MultipartonInteractions:pT0Ref=2.4024', 
#            'MultipartonInteractions:ecmPow=0.25208', 
#            'MultipartonInteractions:expPow=1.6'),
#        pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
#            'Main:timesAllowErrors = 10000', 
#            'Check:epTolErr = 0.01', 
#            'Beams:setProductionScalesFromLHEF = off', 
#            'SLHA:keepSM = on', 
#            'SLHA:minMassSM = 1000.', 
#            'ParticleDecays:limitTau0 = on', 
#            'ParticleDecays:tau0Max = 10', 
#            'ParticleDecays:allowPhotonRadiation = on')
#    ),
#    comEnergy = cms.double(8000.0),
#    filterEfficiency = cms.untracked.double(1.0),
#    maxEventsToPrint = cms.untracked.int32(0),
#    pythiaHepMCVerbosity = cms.untracked.bool(False),
#    pythiaPylistVerbosity = cms.untracked.int32(0)
#)



import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *



process.generator = cms.EDFilter("Pythia8GeneratorFilter",
                         comEnergy = cms.double(13000.0),
                         crossSection = cms.untracked.double(6.44),
                         filterEfficiency = cms.untracked.double(1),
                         maxEventsToPrint = cms.untracked.int32(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         pythiaPylistVerbosity = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
            'NewGaugeBoson:ffbar2gmZZprime = on',
	    'Zprime:gmZmode = 3',
            '32:m0 = 500',
            'PartonLevel:all = on',     
            'PartonLevel:MPI = off',
            'PartonLevel:ISR = off',
            'PartonLevel:FSR = off',
	),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CUEP8M1Settings',
                                    'processParameters',
                                    )
        )
                         )



process.ProductionFilterSequence = cms.Sequence(process.generator)

# Path and EndPath definitions
#     for step1  (gen)
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
#     for step2  (digi2raw)
process.digitisation_step = cms.Path(process.pdigi)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.raw2digi_step = cms.Path(process.RawToDigi)
process.L1Reco_step = cms.Path(process.L1Reco)
#     common to step1 and step2
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RAWSIMoutput_step = cms.EndPath(process.RAWSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,
      process.digitisation_step,process.L1simulation_step,process.digi2raw_step,
      process.endjob_step,process.RAWSIMoutput_step)
#   drop the following from step2.
# process.schedule.extend(process.HLTSchedule)
# process.schedule.extend([process.raw2digi_step,process.L1Reco_step,process.endjob_step,process.RAWSIMoutput_step])

# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.ProductionFilterSequence * getattr(process,path)._seq 

# customisation of the process.
#     drop the customisation section from step 2.
# Automatic addition of the customisation function from HLTrigger.Configuration.customizeHLTforMC
# from HLTrigger.Configuration.customizeHLTforMC import customizeHLTforFullSim

#call to customisation function customizeHLTforFullSim imported from HLTrigger.Configuration.customizeHLTforMC
# process = customizeHLTforFullSim(process)

# End of customisation functions

