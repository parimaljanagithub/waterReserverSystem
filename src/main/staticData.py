from src import db
from src.model.WaterReserverModel import Dam, DemandType


def insert_static_data():
    inser_dam_static_data();
    inser_demand_type_static_data();

def inser_dam_static_data():
    dam_list = []
    dam_list.append(Dam(dam_name='MAHI', active_flag='Y'))
    dam_list.append(Dam(dam_name='KADANA', active_flag='Y'))
    dam_list.append(Dam(dam_name='PANAM', active_flag='Y'))
    #db.session.bulk_save_objects(dam_list)
    #db.session.merge(d)
    for i in range(len(dam_list)) :
        if db.session.query(Dam).filter_by(dam_name=dam_list[i].dam_name).count()<1 :
            db.session.add(dam_list[i])
            db.session.commit()
        else:
            print('Dam data already present')

#possible values  irrigation, hydropower
def inser_demand_type_static_data():
    demand_type_list = []
    demand_type_list.append(DemandType(type='IRRIGATION'))
    demand_type_list.append(DemandType(type='HYDROPOWER'))
    for i in range(len(demand_type_list)) :
        if db.session.query(DemandType).filter_by(type=demand_type_list[i].type).count()<1 :
            db.session.add(demand_type_list[i])
            db.session.commit()
            print('demand type data inserted')
        else:    
            print('demand type data already present')