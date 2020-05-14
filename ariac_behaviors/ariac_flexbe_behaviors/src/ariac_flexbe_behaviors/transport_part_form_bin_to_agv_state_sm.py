#!/usr/bin/env python
# -*- coding: utf-8 -*-
###########################################################
#               WARNING: Generated code!                  #
#              **************************                 #
# Manual changes may get lost if file is generated again. #
# Only code inside the [MANUAL] tags will be kept.        #
###########################################################

from flexbe_core import Behavior, Autonomy, OperatableStateMachine, ConcurrencyContainer, PriorityContainer, Logger
from ariac_logistics_flexbe_states.get_material_locations import GetMaterialLocationsState
from ariac_flexbe_states.message_state import MessageState
from ariac_flexbe_states.srdf_state_to_moveit_ariac_state import SrdfStateToMoveitAriac
from ariac_flexbe_states.vacuum_gripper_state import VacuumGripperControlState
from ariac_support_flexbe_states.replace_state import ReplaceState
from ariac_flexbe_states.detect_part_camera_ariac_state import DetectPartCameraAriacState
from ariac_flexbe_states.compute_grasp_ariac_state import ComputeGraspAriacState
from flexbe_states.wait_state import WaitState
from ariac_flexbe_states.moveit_to_joints_dyn_ariac_state import MoveitToJointsDynAriacState
from ariac_support_flexbe_states.get_item_from_list_state import GetItemFromListState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Wed Apr 22 2020
@author: Gino Goossens
'''
class transport_part_form_bin_to_agv_stateSM(Behavior):
	'''
	transports part from it's bin to the selected agv
	'''


	def __init__(self):
		super(transport_part_form_bin_to_agv_stateSM, self).__init__()
		self.name = 'transport_part_form_bin_to_agv_state'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:1393 y:668, x:704 y:381
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['part_type', 'agv_id', 'pose_on_agv'])
		_state_machine.userdata.part_type = ''
		_state_machine.userdata.agv_id = ''
		_state_machine.userdata.pose_on_agv = []
		_state_machine.userdata.joint_values = []
		_state_machine.userdata.joint_names = []
		_state_machine.userdata.action_topic = '/move_group'
		_state_machine.userdata.move_group = 'manipulator'
		_state_machine.userdata.move_group_prefix = '/ariac/arm1'
		_state_machine.userdata.arm_id = 'arm1'
		_state_machine.userdata.config_name_R1Bin1Pre = 'R1Bin1Pre'
		_state_machine.userdata.config_name_R1AGVPre = 'R1AGVPre'
		_state_machine.userdata.config_name_R2Bin5Pre = 'R2Bin5Pre'
		_state_machine.userdata.robot_name = ''
		_state_machine.userdata.arm2_gebruiken = '/ariac/arm2'
		_state_machine.userdata.part_pose = []
		_state_machine.userdata.part = 'gasket_part'
		_state_machine.userdata.part_offset = 0.030
		_state_machine.userdata.part_drop_offset = 0.1
		_state_machine.userdata.conveyor_power = 100.0
		_state_machine.userdata.part_rotation = 0
		_state_machine.userdata.camera_frame = 'logical_camera_3_frame'
		_state_machine.userdata.camera_topic = '/ariac/logical_camera_3'
		_state_machine.userdata.camera_ref_frame = 'arm1_linear_arm_actuator'
		_state_machine.userdata.tool_link = 'ee_link'
		_state_machine.userdata.bin_location = []
		_state_machine.userdata.material_locations = []
		_state_machine.userdata.zero_value = 0

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:12 y:198
			OperatableStateMachine.add('get part location',
										GetMaterialLocationsState(),
										transitions={'continue': 'bin location'},
										autonomy={'continue': Autonomy.Off},
										remapping={'part': 'part_type', 'material_locations': 'material_locations'})

			# x:305 y:37
			OperatableStateMachine.add('MoseMessage',
										MessageState(),
										transitions={'continue': 'detect object'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'pose_on_agv'})

			# x:171 y:37
			OperatableStateMachine.add('PartTypeMessage',
										MessageState(),
										transitions={'continue': 'MoseMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'part_type'})

			# x:681 y:38
			OperatableStateMachine.add('pre grasp',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'compute grasp', 'planning_failed': 'failed', 'control_failed': 'compute grasp', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1Bin1Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1433 y:179
			OperatableStateMachine.add('move_agv',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'gripper uit', 'planning_failed': 'failed', 'control_failed': 'gripper uit', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R1AGVPre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1255 y:51
			OperatableStateMachine.add('gripper aan',
										VacuumGripperControlState(enable=True),
										transitions={'continue': 'wait', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1405 y:434
			OperatableStateMachine.add('robot_2_selecteren',
										ReplaceState(),
										transitions={'done': 'robot_2_bewegen'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm2_gebruiken', 'result': 'move_group_prefix'})

			# x:1424 y:526
			OperatableStateMachine.add('robot_2_bewegen',
										SrdfStateToMoveitAriac(),
										transitions={'reached': 'finished', 'planning_failed': 'failed', 'control_failed': 'finished', 'param_error': 'failed'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off, 'param_error': Autonomy.Off},
										remapping={'config_name': 'config_name_R2Bin5Pre', 'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'action_topic': 'action_topic', 'robot_name': 'robot_name', 'config_name_out': 'config_name_out', 'move_group_out': 'move_group_out', 'robot_name_out': 'robot_name_out', 'action_topic_out': 'action_topic_out', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:465 y:35
			OperatableStateMachine.add('detect object',
										DetectPartCameraAriacState(time_out=0.5),
										transitions={'continue': 'pre grasp', 'failed': 'failed', 'not_found': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'not_found': Autonomy.Off},
										remapping={'ref_frame': 'camera_ref_frame', 'camera_topic': 'camera_topic', 'camera_frame': 'camera_frame', 'part': 'part', 'pose': 'pose'})

			# x:862 y:38
			OperatableStateMachine.add('compute grasp',
										ComputeGraspAriacState(joint_names=['linear_arm_actuator_joint', 'shoulder_pan_joint', 'shoulder_lift_joint', 'elbow_joint', 'wrist_1_joint', 'wrist_2_joint', 'wrist_3_joint']),
										transitions={'continue': 'pick_positie', 'failed': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off},
										remapping={'move_group': 'move_group', 'move_group_prefix': 'move_group_prefix', 'tool_link': 'tool_link', 'pose': 'pose', 'offset': 'part_offset', 'rotation': 'part_rotation', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:1475 y:50
			OperatableStateMachine.add('wait',
										WaitState(wait_time=1),
										transitions={'done': 'move_agv'},
										autonomy={'done': Autonomy.Off})

			# x:1414 y:297
			OperatableStateMachine.add('gripper uit',
										VacuumGripperControlState(enable=False),
										transitions={'continue': 'robot_2_selecteren', 'failed': 'failed', 'invalid_arm_id': 'failed'},
										autonomy={'continue': Autonomy.Off, 'failed': Autonomy.Off, 'invalid_arm_id': Autonomy.Off},
										remapping={'arm_id': 'arm_id'})

			# x:1047 y:40
			OperatableStateMachine.add('pick_positie',
										MoveitToJointsDynAriacState(),
										transitions={'reached': 'gripper aan', 'planning_failed': 'failed', 'control_failed': 'gripper aan'},
										autonomy={'reached': Autonomy.Off, 'planning_failed': Autonomy.Off, 'control_failed': Autonomy.Off},
										remapping={'move_group_prefix': 'move_group_prefix', 'move_group': 'move_group', 'action_topic': 'action_topic', 'joint_values': 'joint_values', 'joint_names': 'joint_names'})

			# x:150 y:300
			OperatableStateMachine.add('bin location',
										GetItemFromListState(),
										transitions={'done': 'AgvIdMessage', 'invalid_index': 'failed'},
										autonomy={'done': Autonomy.Off, 'invalid_index': Autonomy.Off},
										remapping={'list': 'material_locations', 'index': 'zero_value', 'item': 'bin_location'})

			# x:176 y:126
			OperatableStateMachine.add('AgvIdMessage',
										MessageState(),
										transitions={'continue': 'PartTypeMessage'},
										autonomy={'continue': Autonomy.Off},
										remapping={'message': 'agv_id'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
