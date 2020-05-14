#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.start_assignment_state import StartAssignment
from ariac_logistics_flexbe_states.get_order_state import GetOrderState
from ariac_logistics_flexbe_states.get_products_from_shipment_state import GetProductsFromShipmentState
from ariac_logistics_flexbe_states.get_part_from_products_state import GetPartFromProductsState
from ariac_support_flexbe_states.add_numeric_state import AddNumericState
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_behaviors.notify_shipment_ready_sm import notify_shipment_readySM
from ariac_flexbe_behaviors.transport_part_form_bin_to_agv_state_sm import transport_part_form_bin_to_agv_stateSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 12 2020
@author: gino
'''
class testSM(Behavior):
	'''
	robotwisseltest
	'''


	def __init__(self):
		super(testSM, self).__init__()
		self.name = 'test'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(notify_shipment_readySM, 'notify_shipment_ready')
		self.add_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:509 y:35, x:204 y:373
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.shipments = []
		_state_machine.userdata.number_of_shipments = 0
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.shipment_type = ''
		_state_machine.userdata.products = []
		_state_machine.userdata.number_of_products = 0
		_state_machine.userdata.shipment_index = 0
		_state_machine.userdata.product_index = 0
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.one_value = 1
		_state_machine.userdata.zero_value = 0
		_state_machine.userdata.order_id = ''
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.old_order_id = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:65 y:95
			OperatableStateMachine.add('start',
										StartAssignment(),
										transitions={'continue': 'getorder'},
										autonomy={'continue': Autonomy.Off})

			# x:243 y:92
			OperatableStateMachine.add('getorder',
										GetOrderState(),
										transitions={'continue': 'compare_last_order'},
										autonomy={'continue': Autonomy.Off},
										remapping={'order_id': 'order_id', 'shipments': 'shipments', 'number_of_shipments': 'number_of_shipments'})

			# x:465 y:94
			OperatableStateMachine.add('get_products_from_shipments',
										GetProductsFromShipmentState(),
										transitions={'continue': 'get_part_from_products', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'shipments': 'shipments', 'index': 'shipment_index', 'shipment_type': 'shipment_type', 'agv_id': 'agv_id', 'products': 'products', 'number_of_products': 'number_of_products'})

			# x:689 y:90
			OperatableStateMachine.add('get_part_from_products',
										GetPartFromProductsState(),
										transitions={'continue': 'transport_part_form_bin_to_agv_state', 'invalid_index': 'failed'},
										autonomy={'continue': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'products': 'products', 'index': 'product_index', 'type': 'part_type', 'pose': 'part_pose'})

			# x:986 y:193
			OperatableStateMachine.add('increment_product_index',
										AddNumericState(),
										transitions={'done': 'einde_products'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'one_value', 'result': 'product_index'})

			# x:978 y:283
			OperatableStateMachine.add('einde_products',
										EqualState(),
										transitions={'true': 'reset_product index', 'false': 'get_part_from_products'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'product_index', 'value_b': 'number_of_products'})

			# x:972 y:480
			OperatableStateMachine.add('increment_shipment_index',
										AddNumericState(),
										transitions={'done': 'einde_shipments'},
										autonomy={'done': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'one_value', 'result': 'shipment_index'})

			# x:971 y:579
			OperatableStateMachine.add('einde_shipments',
										EqualState(),
										transitions={'true': 'notify_shipment_ready', 'false': 'get_products_from_shipments'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'shipment_index', 'value_b': 'number_of_shipments'})

			# x:978 y:384
			OperatableStateMachine.add('reset_product index',
										ReplaceState(),
										transitions={'done': 'increment_shipment_index'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'zero_value', 'result': 'product_index'})

			# x:572 y:362
			OperatableStateMachine.add('notify_shipment_ready',
										self.use_behavior(notify_shipment_readySM, 'notify_shipment_ready'),
										transitions={'finished': 'get_products_from_shipments', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit})

			# x:959 y:86
			OperatableStateMachine.add('transport_part_form_bin_to_agv_state',
										self.use_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state'),
										transitions={'finished': 'increment_product_index', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'part_pose'})

			# x:266 y:2
			OperatableStateMachine.add('compare_last_order',
										EqualState(),
										transitions={'true': 'finished', 'false': 'rememberoldorder'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'order_id', 'value_b': 'old_order_id'})

			# x:584 y:4
			OperatableStateMachine.add('rememberoldorder',
										ReplaceState(),
										transitions={'done': 'get_products_from_shipments'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'order_id', 'result': 'old_order_id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
