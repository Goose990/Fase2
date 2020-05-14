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
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Thu May 14 2020
@author: Gino Goossens
'''
class Nieuwe_camerapregrasp_behaviorSM(Behavior):
	'''
	zet robot in juiste pregrasp en selecteerd de juiste camera
	'''


	def __init__(self):
		super(Nieuwe_camerapregrasp_behaviorSM, self).__init__()
		self.name = 'Nieuwe_camera/pre-grasp_behavior'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1642 y:212, x:296 y:570
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type'], output_keys=['part_offset_goal', 'camera_frame_goal', 'camera_ref_frame_goal', 'camera_topic_goal'])
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.camera_ref_frame_goal = ''
		_state_machine.userdata.camera_topic_goal = ''
		_state_machine.userdata.camera_frame_goal = ''
		_state_machine.userdata.part1 = 'gasket_part'
		_state_machine.userdata.part2 = 'pulley_part'
		_state_machine.userdata.part3 = 'piston_rod_part'
		_state_machine.userdata.part4 = 'gear_part'
		_state_machine.userdata.config_name_R1Bin1Pre = 'R1Bin1Pre'
		_state_machine.userdata.config_name_R1Bin2Pre = 'R1Bin2Pre'
		_state_machine.userdata.config_name_R2Bin5Pre = 'R2Bin5Pre'
		_state_machine.userdata.config_name_R2Bin6Pre = R2Bin6Pre
		_state_machine.userdata.move_group_prefix1 = '/ariac/arm1'
		_state_machine.userdata.move_group_prefix2 = '/ariac/arm2'
		_state_machine.userdata.camera_ref_frame1 = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_ref_frame2 = 'arm2_linear_arm_actuator'
		_state_machine.userdata.camera_topic1 = '/ariac/logical_camera_3'
		_state_machine.userdata.camera_topic2 = '/ariac/logical_camera_4'
		_state_machine.userdata.camera_topic3 = '/ariac/logical_camera_7'
		_state_machine.userdata.camera_topic4 = '/ariac/logical_camera_8'
		_state_machine.userdata.camera_frame1 = 'logical_camera_3_frame'
		_state_machine.userdata.camera_frame2 = 'logical_camera_4_frame'
		_state_machine.userdata.camera_frame3 = 'logical_camera_7_frame'
		_state_machine.userdata.camera_frame4 = 'logical_camera_8_frame'
		_state_machine.userdata.part_offset_goal = ''
		_state_machine.userdata.part1_offset = 0.03
		_state_machine.userdata.part2_offset = 0.08
		_state_machine.userdata.part3_offset = 0.02
		_state_machine.userdata.part4_offset = 0.03
		_state_machine.userdata.part_type = ''

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

			# x:431 y:33
			OperatableStateMachine.add('pre_grasp_1',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'set_camera_ref_frame', 'planning_failed': 'failed', 'control_failed': 'retry', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1Bin1Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:891 y:490
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

			# x:433 y:124
			OperatableStateMachine.add('pre_grasp_2',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'set_camera_ref_frame_2', 'planning_failed': 'failed', 'control_failed': 'retry_2', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1Bin2Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix1', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:80 y:232
			OperatableStateMachine.add('vergelijk_3',
										EqualState(),
										transitions={'true': 'pre_grasp_3', 'false': 'vergelijk_4'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part3'})

			# x:434 y:209
			OperatableStateMachine.add('pre_grasp_3',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'set_camera_ref_frame_3', 'planning_failed': 'failed', 'control_failed': 'retry_3', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R2Bin5Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:77 y:332
			OperatableStateMachine.add('vergelijk_4',
										EqualState(),
										transitions={'true': 'pre_grasp_4', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'part_type', 'value_b': 'part4'})

			# x:436 y:296
			OperatableStateMachine.add('pre_grasp_4',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'set_camera_ref_frame_4', 'planning_failed': 'failed', 'control_failed': 'retry_4', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R2Bin6Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix2', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:722 y:50
			OperatableStateMachine.add('set_camera_ref_frame',
										ReplaceState(),
										transitions={'done': 'set_camera_topic'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame1', 'result': 'camera_ref_frame_goal'})

			# x:934 y:46
			OperatableStateMachine.add('set_camera_topic',
										ReplaceState(),
										transitions={'done': 'set_camera_frame'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic1', 'result': 'camera_topic_goal'})

			# x:1146 y:46
			OperatableStateMachine.add('set_camera_frame',
										ReplaceState(),
										transitions={'done': 'set_part_offset_1'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame1', 'result': 'camera_frame_goal'})

			# x:723 y:128
			OperatableStateMachine.add('set_camera_ref_frame_2',
										ReplaceState(),
										transitions={'done': 'set_camera_topic_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame1', 'result': 'camera_ref_frame_goal'})

			# x:937 y:129
			OperatableStateMachine.add('set_camera_topic_2',
										ReplaceState(),
										transitions={'done': 'set_camera_frame_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic2', 'result': 'camera_topic_goal'})

			# x:1144 y:125
			OperatableStateMachine.add('set_camera_frame_2',
										ReplaceState(),
										transitions={'done': 'set_part_offset_2'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame2', 'result': 'camera_frame_goal'})

			# x:723 y:213
			OperatableStateMachine.add('set_camera_ref_frame_3',
										ReplaceState(),
										transitions={'done': 'set_camera_topic_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame2', 'result': 'camera_ref_frame_goal'})

			# x:938 y:211
			OperatableStateMachine.add('set_camera_topic_3',
										ReplaceState(),
										transitions={'done': 'set_camera_frame_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic3', 'result': 'camera_topic_goal'})

			# x:1148 y:210
			OperatableStateMachine.add('set_camera_frame_3',
										ReplaceState(),
										transitions={'done': 'set_part_offset_3'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame3', 'result': 'camera_frame_goal'})

			# x:723 y:299
			OperatableStateMachine.add('set_camera_ref_frame_4',
										ReplaceState(),
										transitions={'done': 'set_camera_topic_4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_ref_frame2', 'result': 'camera_ref_frame_goal'})

			# x:939 y:297
			OperatableStateMachine.add('set_camera_topic_4',
										ReplaceState(),
										transitions={'done': 'set_camera_frame_4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_topic4', 'result': 'camera_topic_goal'})

			# x:1148 y:296
			OperatableStateMachine.add('set_camera_frame_4',
										ReplaceState(),
										transitions={'done': 'set_part_offset_4'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'camera_frame4', 'result': 'camera_frame_goal'})

			# x:1336 y:48
			OperatableStateMachine.add('set_part_offset_1',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'part1_offset', 'result': 'part_offset_goal'})

			# x:1334 y:302
			OperatableStateMachine.add('set_part_offset_4',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'part4_offset', 'result': 'part_offset_goal'})

			# x:1336 y:125
			OperatableStateMachine.add('set_part_offset_2',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'part2_offset', 'result': 'part_offset_goal'})

			# x:1332 y:210
			OperatableStateMachine.add('set_part_offset_3',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'part3_offset', 'result': 'part_offset_goal'})

			# x:891 y:552
			OperatableStateMachine.add('retry_2',
										WaitState(wait_time=0.5),
										transitions={'done': 'pre_grasp_2'},
										autonomy={'done': Autonomy.Off})

			# x:891 y:629
			OperatableStateMachine.add('retry_3',
										WaitState(wait_time=0.5),
										transitions={'done': 'pre_grasp_3'},
										autonomy={'done': Autonomy.Off})

			# x:891 y:706
			OperatableStateMachine.add('retry_4',
										WaitState(wait_time=0.5),
										transitions={'done': 'pre_grasp_4'},
										autonomy={'done': Autonomy.Off})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
