#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_flexbe_states.vacuum_gripper_state import VacuumGripperControlState
from flexbe_states.wait_state import WaitState
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

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1592 y:474, x:550 y:380
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'])
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.config_name_R1BinPre = 'R1Bin1Pre'
		_state_machine.userdata.config_name_R1AGVPre = 'R1AGVPre'
		_state_machine.userdata.config_name_R2Bin5Pre = 'R2Bin5Pre'
		_state_machine.userdata.move_group_prefix = '/ariac/arm1'
		_state_machine.userdata.arm2 = '/ariac/arm2'
		_state_machine.userdata.arm_id = 'arm1'
		_state_machine.userdata.gripper_2 = 'arm2'
		_state_machine.userdata.camera_ref_frame = 'arm1_linear_arm_actuator'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_3'
		_state_machine.userdata.camera_frame = 'logical_camera_3_frame'
		_state_machine.userdata.part_offset = 0.035
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.part = 'gasket_part'

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:10 y:138
			OperatableStateMachine.add('detect part',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'move', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'part_pose'})

			# x:1539 y:192
			OperatableStateMachine.add('robot_2_bewegen',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'finished', 'control_failed': 'finished', 'param_error': 'finished'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R2Bin5Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1118 y:129
			OperatableStateMachine.add('move_agv',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'robot_2_selecteren', 'planning_failed': 'failed', 'control_failed': 'robot_2_selecteren', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1AGVPre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1215 y:307
			OperatableStateMachine.add('robot_2_selecteren',
										ReplaceState(),
										transitions={'done': 'robot_2_bewegen'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm2', 'result': 'move_group_prefix'})

			# x:334 y:175
			OperatableStateMachine.add('compute pick',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'R1_oppakken', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'part_pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:525 y:160
			OperatableStateMachine.add('R1_oppakken',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'gripper aan', 'planning_failed': 'failed', 'control_failed': 'gripper aan'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:743 y:210
			OperatableStateMachine.add('gripper aan',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'wacht', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:945 y:153
			OperatableStateMachine.add('wacht',
										WaitState(wait_time=1),
										transitions={'done': 'move_agv'},
										autonomy={'done': Autonomy.Off})

			# x:185 y:59
			OperatableStateMachine.add('move',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'compute pick', 'planning_failed': 'failed', 'control_failed': 'compute pick', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1BinPre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
