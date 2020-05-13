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
from ariac_flexbe_states.end_assignment_state import EndAssignment
from ariac_flexbe_behaviors.transport_part_form_bin_to_agv_state_sm import transport_part_form_bin_to_agv_stateSM
from ariac_flexbe_behaviors.arm_selector_sm import arm_selectorSM
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gino en Leon
'''
class transport_part_from_bin_to_agv_1SM(Behavior):
	'''
	Transorts a part vorm it's bin to the selecte agv
	'''


	def __init__(self):
		super(transport_part_from_bin_to_agv_1SM, self).__init__()
		self.name = 'transport_part_from_bin_to_agv_1'

		# parameters of this behavior

		# references to used behaviors
		self.add_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state')
		self.add_behavior(arm_selectorSM, 'arm_selector')

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:845 y:63, x:414 y:193
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.agv_id = 'agv1'
		_state_machine.userdata.part_type = 'gear_part'
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.config_name_home = 'home'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.config_name_R2Bin4Pre = 'R2Bin4Pre'
		_state_machine.userdata.arm_id = 'arm1'
		_state_machine.userdata.move_group_prefix = '/ariac/arm1'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:52 y:43
			OperatableStateMachine.add('StartAssignment',
										StartAssignment(),
										transitions={'continue': 'arm_selector'},
										autonomy={'continue': Autonomy.Off})

			# x:625 y:49
			OperatableStateMachine.add('EndAssignment',
										EndAssignment(),
										transitions={'continue': 'finished'},
										autonomy={'continue': Autonomy.Off})

			# x:326 y:46
			OperatableStateMachine.add('transport_part_form_bin_to_agv_state',
										self.use_behavior(transport_part_form_bin_to_agv_stateSM, 'transport_part_form_bin_to_agv_state'),
										transitions={'finished': 'EndAssignment', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'part_type': 'part_type', 'agv_id': 'agv_id', 'pose_on_agv': 'pose_on_agv', 'move_group_prefix': 'move_group_prefix'})

			# x:177 y:125
			OperatableStateMachine.add('arm_selector',
										self.use_behavior(arm_selectorSM, 'arm_selector'),
										transitions={'finished': 'transport_part_form_bin_to_agv_state', 'failed': 'failed'},
										autonomy={'finished': Autonomy.Inherit, 'failed': Autonomy.Inherit},
										remapping={'arm_id': 'arm_id', 'move_group_prefix': 'move_group_prefix'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
