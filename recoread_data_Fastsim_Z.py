
import FWCore.ParameterSet.Config as cms  

process = cms.Process ("HcalReco")
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')



#process.GlobalTag.globaltag = 'GR_P_V56::All'
process.GlobalTag.globaltag = 'MCRUN2_74_V9::All'
#process.GlobalTag = GlobalTag(process.GlobalTag, 'GR_E_V48', '')
#process.GlobalTag.globaltag = 'START62_V1::All'
#from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:mc', '')


process.maxEvents = cms.untracked.PSet( 
    input = cms.untracked.int32(-1)
) 
process.MessageLogger = cms.Service('MessageLogger', 
 cout = cms.untracked.PSet( 
  default = cms.untracked.PSet( ## kill all messages in the log
 
   limit = cms.untracked.int32(0) 
  ),  
  FwkJob = cms.untracked.PSet( ## but FwkJob category - those unlimitted 
 
   limit = cms.untracked.int32(-1)  
  ) 
 ),  
 categories = cms.untracked.vstring('FwkJob'),
 destinations = cms.untracked.vstring('cout')
) 
#process.MessageLogger.cerr.FwkReport.reportEvery = 10

process.source = cms.Source('PoolSource',
    fileNames = cms.untracked.vstring(

'file:recosim_Zprime_1.root'

 )
#,  skipEvents=cms.untracked.uint32(5000)
) 

process.TFileService = cms.Service("TFileService",
 fileName = cms.string('hist_recoread_Fullsim_Z_jpt.root'),                                   
)

process.hcalreco = cms.EDAnalyzer("HcalRecoReader",
#GammaJetAnalysis = cms.EDAnalyzer('GammaJetAnalysis',
CaloJetCollection=cms.untracked.InputTag("ak4CaloJets"),
  RootFileName = cms.untracked.string('hcalrecoread_data2.root'),                                  
  RECO =  cms.untracked.bool(True),
  IndEnergy =  cms.untracked.bool(True),
  Position =  cms.untracked.bool(True),                               
  genJetCollName      = cms.string('ak4GenJets'),
  genParticleCollName = cms.string('genParticles'),
   genEventInfoName    = cms.string('generator')
#)
)

#   met for Run1 and caloMet for Run2...
process.hcalnoiseinfoanalyzer = cms.EDAnalyzer(
    'HcalNoiseInfoAnalyzer',
    rbxCollName = cms.string('hcalnoise'),
    MetTag     = cms.untracked.InputTag( 'caloMet' ),
    SkipLumiBlocks = cms.double(0),
    NumLumiBlocks = cms.double(5000)
)

process.p1 = cms.Path(process.hcalreco*process.hcalnoiseinfoanalyzer)

