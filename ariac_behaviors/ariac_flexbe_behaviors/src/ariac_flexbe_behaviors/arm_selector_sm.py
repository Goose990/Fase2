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
from ariac_support_flexbe_states.replace_state import ReplaceState
# Additional imports can be added inside the following tags
# [MANUAL_IMPORT]

# [/MANUAL_IMPORT]


'''
Created on Tue May 12 2020
@author: gino
'''
class arm_selectorSM(Behavior):
	'''
	mooi
	'''


	def __init__(self):
		super(arm_selectorSM, self).__init__()
		self.name = 'arm_selector'

		# parameters of this behavior

		# references to used behaviors

		# Additional initialization code can be added inside the following tags
		# [MANUAL_INIT]
		
		# [/MANUAL_INIT]

		# Behavior comments:



	def create(self):
		# x:615 y:109, x:113 y:271
		_state_machine = OperatableStateMachine(outcomes=['finished', 'failed'], input_keys=['arm_id'], output_keys=['move_group_prefix'])
		_state_machine.userdata.prefix_arm1 = '/ariac/arm1'
		_state_machine.userdata.prefix_arm2 = '/ariac/arm2'
		_state_machine.userdata.arm1 = 'arm1'
		_state_machine.userdata.arm2 = 'arm2'
		_state_machine.userdata.arm_id = ''
		_state_machine.userdata.move_group_prefix = ''

		# Additional creation code can be added inside the following tags
		# [MANUAL_CREATE]
		
		# [/MANUAL_CREATE]


		with _state_machine:
			# x:54 y:52
			OperatableStateMachine.add('compare_1',
										EqualState(),
										transitions={'true': 'Value_1', 'false': 'compare_1_2'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'arm1'})

			# x:319 y:58
			OperatableStateMachine.add('Value_1',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm_id', 'result': 'prefix_arm1'})

			# x:53 y:150
			OperatableStateMachine.add('compare_1_2',
										EqualState(),
										transitions={'true': 'Value_1_2', 'false': 'failed'},
										autonomy={'true': Autonomy.Off, 'false': Autonomy.Off},
										remapping={'value_a': 'arm_id', 'value_b': 'arm2'})

			# x:318 y:155
			OperatableStateMachine.add('Value_1_2',
										ReplaceState(),
										transitions={'done': 'finished'},
										autonomy={'done': Autonomy.Off},
										remapping={'value': 'arm_id', 'result': 'prefix_arm2'})


		return _state_machine


	# Private functions can be added inside the following tags
	# [MANUAL_FUNC]
	
	# [/MANUAL_FUNC]
