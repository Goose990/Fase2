#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_support_flexbe_states.equal_state import EqualState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from flexbe_states.wait_state import WaitState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed May 13 2020
@author: gino
'''
class bewegen_naar_pregraspSM(Behavior):
	'''
	identificeert het parttype en gaat naar de juiste pregrasp
	'''


	def __init__(self):
		super(bewegen_naar_pregraspSM, self).__init__()
		self.name = 'bewegen_naar_pregrasp'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1576 y:101, x:293 y:572
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.move_group_prefix1 = '/ariac/arm1'
		_state_machine.userdata.move_group_prefix2 = '/ariac/arm2'
		_state_machine.userdata.part1 = 'gasket_part'
		_state_machine.userdata.part2 = 'pulley_part'
		_state_machine.userdata.part3 = 'piston_rod_part'
		_state_machine.userdata.part4 = 'gear_part'
		_state_machine.userdata.config_name_R1Bin1Pre = 'R1Bin1Pre'
		_state_machine.userdata.config_name_R1Bin2Pre = 'R1Bin2Pre'
		_state_machine.userdata.config_name_R2Bin5Pre = 'R2Bin5Pre'
		_state_machine.userdata.config_name_R2Bin6Pre = 'R2Bin6Pre'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:85 y:38
			OperatableStateMachine.add('vergelijk',
										EqualState(),
										transitions={'true': 'pre_grasp_1', 'false': 'vergelijk_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part1'})

			# x:497 y:53
			OperatableStateMachine.add('pre_grasp_1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1Bin1Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1554 y:628
			OperatableStateMachine.add('retry',
										WaitState(wait_time=0.5),
										transitions={'done': 'pre_grasp_1'},
										autonomy={'done': Autonomy.Off})

			# x:82 y:134
			OperatableStateMachine.add('vergelijk_2',
										EqualState(),
										transitions={'true': 'pre_grasp_2', 'false': 'vergelijk_3'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part2'})

			# x:499 y:114
			OperatableStateMachine.add('pre_grasp_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1Bin2Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:80 y:232
			OperatableStateMachine.add('vergelijk_3',
										EqualState(),
										transitions={'true': 'pre_grasp_3', 'false': 'vergelijk_4'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part3'})

			# x:498 y:174
			OperatableStateMachine.add('pre_grasp_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R2Bin5Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:77 y:332
			OperatableStateMachine.add('vergelijk_4',
										EqualState(),
										transitions={'true': 'pre_grasp_4', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part4'})

			# x:497 y:237
			OperatableStateMachine.add('pre_grasp_4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R2Bin6Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
