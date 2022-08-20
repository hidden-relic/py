from draftsman.blueprintable import Blueprint
from draftsman import entity
from draftsman import constants

bp=Blueprint()

assemblers=[]
inserters_in=[]
inserters_out=[]
rails=[]

assembler=entity.AssemblingMachine('assembling-machine-2')
assemblers.append(assembler)
inserter_in=entity.Inserter('fast-inserter')
inserter_in.position=assembler.position+(3,1)
inserter_in.direction=constants.Direction['EAST']
inserter_out=entity.Inserter('fast-inserter')
inserter_out.position=inserter_in.position+(0,1)
inserter_out.direction=constants.Direction['WEST']
inserters_in.append(inserter_in)
inserters_out.append(inserter_out)
[bp.entities.append(x) for x in assemblers]
[bp.entities.append(x) for x in inserters_in]
[bp.entities.append(x) for x in inserters_out]

print(bp.to_dict())