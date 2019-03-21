# ----------------------------------------------
# Script Recorded by ANSYS Electronics Desktop Version 2018.1.0
# 17:35:24  Mar 19, 2019
# ----------------------------------------------
import ScriptEnv
import json

f = open("C:\Users\dothe\Documents\Ansoft\patch.json")
j = json.load(f)

ScriptEnv.Initialize("Ansoft.ElectronicsDesktop")
oDesktop.RestoreWindow()
oProject = oDesktop.NewProject()
oProject.Rename("C:/Users/dothe/Documents/Ansoft/Generated_Patch.aedt", True)
oProject.InsertDesign("HFSS", "HFSSDesign1", "DrivenModal", "")
oDesign = oProject.SetActiveDesign("HFSSDesign1")
oDesign.RenameDesignInstance("HFSSDesign1", "Patch1")
oDesign.SetSolutionType("DrivenTerminal", False)
oProject.Save()
oEditor = oDesign.SetActiveEditor("3D Modeler")

#### VARIABLES
oDesign.ChangeProperty(
	[
		"NAME:AllTabs",
		[
			"NAME:LocalVariableTab",
			[
				"NAME:PropServers", 
				"LocalVariables"
			],
			[
				"NAME:NewProps",
				[
					"NAME:subs_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['substrate']['length']) + "cm"
				],
				[
					"NAME:subs_w",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['substrate']['width']) + "cm"
				],
				[
					"NAME:h",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['substrate']['height']) + "cm"
				],
				[
					"NAME:pat_l",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['patch']['length']) + "cm"
				],
				[
					"NAME:pat_w",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['patch']['width']) + "cm"
				],
				[
					"NAME:x0",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['patch']['inset_depth']) + "cm"
				],
				[
					"NAME:y0",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['patch']['notch_width']*2+j['patch']['feed_width']) + "cm"
				],
				[
					"NAME:w50",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['patch']['feed_width']) + "cm"
				],
				[
					"NAME:l50",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, "subs_l/2-(pat_l/2-x0)"
				],
				[
					"NAME:QW",
					"PropType:="		, "VariableProp",
					"UserDef:="		, True,
					"Value:="		, str(j['quarter_wave']) + "cm"
				]
			]
		]
	])
	
#### SUBSTRATE
oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-subs_l/2",
		"YPosition:="		, "-subs_w/2",
		"ZPosition:="		, "0mm",
		"XSize:="		, "subs_l",
		"YSize:="		, "subs_w",
		"ZSize:="		, "-h"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Substrate",
		"Flags:="		, "",
		"Color:="		, "(128 128 128)",
		"Transparency:="	, 0.8,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"Al2_O3_ceramic\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	
#### GROUND PLANE
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-subs_l/2",
		"YStart:="		, "-subs_w/2",
		"ZStart:="		, "-h",
		"Width:="		, "subs_l",
		"Height:="		, "subs_w",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Ground_Plane",
		"Flags:="		, "",
		"Color:="		, "(0 128 0)",
		"Transparency:="	, 0.4,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	
#### PATCH
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "-pat_l/2",
		"YStart:="		, "-pat_w/2",
		"ZStart:="		, "0mm",
		"Width:="		, "pat_l",
		"Height:="		, "pat_w",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Patch",
		"Flags:="		, "",
		"Color:="		, "(255 128 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	
#### NOTCH
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "pat_l/2 - x0",
		"YStart:="		, "-y0/2",
		"ZStart:="		, "0mm",
		"Width:="		, "x0",
		"Height:="		, "y0",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Notch",
		"Flags:="		, "",
		"Color:="		, "(143 175 143)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])

#### SUBTRACT GAP FROM PATCH
oEditor.Subtract(
	[
		"NAME:Selections",
		"Blank Parts:="		, "Patch",
		"Tool Parts:="		, "Notch"
	], 
	[
		"NAME:SubtractParameters",
		"KeepOriginals:="	, False
	])

#### FEED LINE
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "pat_l/2-x0",
		"YStart:="		, "-w50/2",
		"ZStart:="		, "0mm",
		"Width:="		, "l50",
		"Height:="		, "w50",
		"WhichAxis:="		, "Z"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Feed",
		"Flags:="		, "",
		"Color:="		, "(255 128 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	
#### JOIN FEED WITH PATCH
oEditor.Unite(
	[
		"NAME:Selections",
		"Selections:="		, "Patch,Feed"
	], 
	[
		"NAME:UniteParameters",
		"KeepOriginals:="	, False
	])
	
#### SOURCE
oEditor.CreateRectangle(
	[
		"NAME:RectangleParameters",
		"IsCovered:="		, True,
		"XStart:="		, "subs_l/2",
		"YStart:="		, "-w50/2",
		"ZStart:="		, "0mm",
		"Width:="		, "w50",
		"Height:="		, "-h",
		"WhichAxis:="		, "X"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Source",
		"Flags:="		, "",
		"Color:="		, "(0 255 0)",
		"Transparency:="	, 0,
		"PartCoordinateSystem:=", "Global",
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	
#### AIR

oEditor.CreateBox(
	[
		"NAME:BoxParameters",
		"XPosition:="		, "-subs_l/2",
		"YPosition:="		, "-subs_w/2",
		"ZPosition:="		, "0mm",
		"XSize:="		, "subs_l",
		"YSize:="		, "subs_w",
		"ZSize:="		, "QW"
	], 
	[
		"NAME:Attributes",
		"Name:="		, "Air",
		"Flags:="		, "",
		"Color:="		, "(0 0 0)",
		"Transparency:="	, 1,
		"PartCoordinateSystem:=", "Global",
		"Display Wireframe:=", True,
		"UDMId:="		, "",
		"MaterialValue:="	, "\"vacuum\"",
		"SurfaceMaterialValue:=", "\"\"",
		"SolveInside:="		, True,
		"IsMaterialEditable:="	, True,
		"UseMaterialAppearance:=", False,
		"IsLightweight:="	, False
	])
	
#### PERFECT E BOUNDARIES
oModule = oDesign.GetModule("BoundarySetup")

oModule.AssignPerfectE(
	[
		"NAME:PerfE_Ground",
		"Objects:="		, ["Ground_Plane"],
		"InfGroundPlane:="	, False
	])
oModule.AssignPerfectE(
	[
		"NAME:PerfE_Patch",
		"Objects:="		, ["Patch"],
		"InfGroundPlane:="	, False
	])
	
#### SOURCE PORT EXCITATION
oModule.AutoIdentifyPorts(
	[
		"NAME:Faces", 
		105
	], False, 
	[
		"NAME:ReferenceConductors", 
		"Ground_Plane"
	], "P1", True)
oModule.RenameBoundary("Patch_T1", "1")

#### RADIATION BOUNDARY
oModule.AssignRadiation(
	[
		"NAME:Radiation",
		"Faces:="		, [108,110,111,112,113],
		"IsFssReference:="	, False,
		"IsForPML:="		, False
	])

#### SOLUTION SETUP
oModule = oDesign.GetModule("AnalysisSetup")
oModule.InsertSetup("HfssDriven", 
	[
		"NAME:Setup1",
		"AdaptMultipleFreqs:="	, False,
		"Frequency:="		, "10GHz",
		"MaxDeltaS:="		, 0.02,
		"PortsOnly:="		, False,
		"UseMatrixConv:="	, False,
		"MaximumPasses:="	, 10,
		"MinimumPasses:="	, 1,
		"MinimumConvergedPasses:=", 1,
		"PercentRefinement:="	, 30,
		"IsEnabled:="		, True,
		"BasisOrder:="		, 1,
		"DoLambdaRefine:="	, True,
		"DoMaterialLambda:="	, True,
		"SetLambdaTarget:="	, False,
		"Target:="		, 0.3333,
		"UseMaxTetIncrease:="	, False,
		"PortAccuracy:="	, 2,
		"UseABCOnPort:="	, False,
		"SetPortMinMaxTri:="	, False,
		"UseDomains:="		, False,
		"UseIterativeSolver:="	, False,
		"SaveRadFieldsOnly:="	, False,
		"SaveAnyFields:="	, True,
		"IESolverType:="	, "Auto",
		"LambdaTargetForIESolver:=", 0.15,
		"UseDefaultLambdaTgtForIESolver:=", True
	])
oModule.InsertFrequencySweep("Setup1", 
	[
		"NAME:Sweep",
		"IsEnabled:="		, True,
		"RangeType:="		, "LinearStep",
		"RangeStart:="		, "8GHz",
		"RangeEnd:="		, "12GHz",
		"RangeStep:="		, "0.01GHz",
		"Type:="		, "Discrete",
		"SaveFields:="		, True,
		"SaveRadFields:="	, False,
		"ExtrapToDC:="		, False
	])
oModule = oDesign.GetModule("RadField")
oModule.InsertFarFieldSphereSetup(
	[
		"NAME:Infinite Sphere1",
		"UseCustomRadiationSurface:=", False,
		"ThetaStart:="		, "0deg",
		"ThetaStop:="		, "180deg",
		"ThetaStep:="		, "10deg",
		"PhiStart:="		, "0deg",
		"PhiStop:="		, "360deg",
		"PhiStep:="		, "10deg",
		"UseLocalCS:="		, False
	])
oProject.Save()
