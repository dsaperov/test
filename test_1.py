from unittest.mock import Mock
import test

test.vk_apigfdf = Mock(return_value='MOCK')
test.f()
