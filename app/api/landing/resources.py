from app.api.commons.base_resource import BaseResource
from app.config import constants


class Landing(BaseResource):

    def get(self):
        print('test: print statement')

        self.LOGGER.debug('test: log in debug mode')
        self.LOGGER.info('test: log in info mode')
        self.LOGGER.warning('test: log in warning mode')
        self.LOGGER.warn('test: log in warn mode')
        self.LOGGER.error('test: log in error mode')
        self.LOGGER.fatal('test: log in fatal mode')
        self.LOGGER.critical('test: log in critical mode')

        return constants.DEFAULT_SUCCESS_HTTP_RESPONSE
