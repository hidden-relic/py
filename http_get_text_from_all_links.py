import requests
from bs4 import BeautifulSoup

urls={'LuaSettings.html', 'Global.html', 'LuaGuiElement.html', 'LuaModuleCategoryPrototype.html', 'LuaForce.html', 'LuaWallControlBehavior.html', 'LuaArithmeticCombinatorControlBehavior.html', 'LuaSurface.html', 'LuaCommandProcessor.html', 'LuaCustomInputPrototype.html', 'Builtin-Types.html', 'LuaEquipment.html', 'LuaHeatBufferPrototype.html', 'LuaParticlePrototype.html', 'Concepts.html', 'LuaFluidEnergySourcePrototype.html', 'LuaBootstrap.html', 'LuaRailChainSignalControlBehavior.html', 'LuaGameScript.html', 'LuaFluidBox.html', 'LuaTrainStopControlBehavior.html', 'LuaVirtualSignalPrototype.html', 'LuaPermissionGroups.html', 'LuaUnitGroup.html', 'LuaContainerControlBehavior.html', 'LuaFluidBoxPrototype.html', 'LuaTechnology.html', 'LuaRandomGenerator.html', 'LuaDecorativePrototype.html', 'LuaCustomChartTag.html', 'LuaStyle.html', 'LuaMiningDrillControlBehavior.html', 'LuaCircuitNetwork.html', 'LuaResourceCategoryPrototype.html', 'LuaNamedNoiseExpression.html', 'LuaChunkIterator.html', 'LuaInserterControlBehavior.html', 'events.html', 'LuaShortcutPrototype.html', 'LuaRCON.html', 'LuaLogisticContainerControlBehavior.html', 'Data-Lifecycle.html', 'index.html', 'LuaEquipmentCategoryPrototype.html', 'LuaItemStack.html', 'LuaTrain.html', 'LuaDamagePrototype.html', 'LuaProfiler.html', 'LuaEquipmentGrid.html', 'LuaProgrammableSpeakerControlBehavior.html', 'LuaFlowStatistics.html', 'LuaLogisticCell.html', 'LuaTilePrototype.html', 'LuaCustomTable.html', 'LuaFluidPrototype.html', 'LuaRailPath.html', 'LuaInventory.html', 'LuaEntity.html', 'defines.html', 'LuaFontPrototype.html', 'LuaControl.html', 'LuaLampControlBehavior.html', 'LuaTechnologyPrototype.html', 'LuaEntityPrototype.html', 'LuaAutoplaceControlPrototype.html', 'LuaControlBehavior.html', 'LuaLazyLoadedValue.html', 'LuaTile.html', 'LuaGui.html', 'LuaHeatEnergySourcePrototype.html', 'LuaPermissionGroup.html', 'LuaRecipePrototype.html', 'LuaDeciderCombinatorControlBehavior.html', 'LuaElectricEnergySourcePrototype.html', 'LuaEquipmentPrototype.html', 'LuaVoidEnergySourcePrototype.html', 'LuaAmmoCategoryPrototype.html', 'LuaTrivialSmokePrototype.html', 'LuaLogisticNetwork.html', 'LuaGenericOnOffControlBehavior.html', 'LuaItemPrototype.html', 'LuaRemote.html', 'LuaAccumulatorControlBehavior.html', 'Libraries.html', 'LuaAISettings.html', 'LuaBurnerPrototype.html', 'LuaRecipeCategoryPrototype.html', 'LuaNoiseLayerPrototype.html', 'LuaRoboportControlBehavior.html', 'LuaCombinatorControlBehavior.html', 'LuaModSettingPrototype.html', 'LuaLogisticPoint.html', 'LuaRecipe.html', 'LuaTransportBeltControlBehavior.html', 'LuaRendering.html', 'LuaConstantCombinatorControlBehavior.html', 'LuaEquipmentGridPrototype.html', 'LuaFuelCategoryPrototype.html', 'LuaPlayer.html', 'LuaTransportLine.html', 'LuaRailSignalControlBehavior.html', 'json-docs.html', 'LuaStorageTankControlBehavior.html', 'LuaGroup.html', 'LuaAchievementPrototype.html', 'Classes.html', 'LuaBurner.html'}
for link in urls:
    url = 'https://lua-api.factorio.com/latest/'+link
    reqs = requests.get(url)
    soup = BeautifulSoup.prettify(BeautifulSoup(reqs.text, 'html.parser'))
    
    prelink="C:\\giz\\fact_api\\"
    
    f=open(prelink+link, 'w')
    f.write(str(soup.encode('utf-8').decode()))
    f.close()
print('done')
# count=0
# for link in urls:
#     count+=1
#     f=open('C:\\giz\\fact_api\\'+str(link.translate(link.maketrans('', '', '#'))), "w")
#     print('grabbing '+str(count)+'\\'+str(len(urls))+'\t'+str(link.translate(link.maketrans('', '', '#'))))
#     reqs=requests.get(str(link))
#     page=BeautifulSoup.prettify(BeautifulSoup(reqs.text, 'html.parser'))
#     # mytable=page.maketrans('\n', chr(32))
#     f.write(page)
#     f.close()