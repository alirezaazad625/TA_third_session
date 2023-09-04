import abc


class DataSource(abc.ABC):
    @abc.abstractmethod
    def write_data(self, data):
        pass

    @abc.abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self.file_name = filename

    def write_data(self, data):
        pass  # writing to file here

    def read_data(self):
        pass  # reading and returning data from file


class DataSourceDecorator(DataSource):

    def __init__(self, source: DataSource):
        self.wrappee = source

    def write_data(self, data):
        self.wrappee.write_data(data)

    def read_data(self):
        return self.wrappee.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        encrypted_data = self.encrypt_data(data)
        self.wrappee.write_data(encrypted_data)

    def encrypt_data(self, data) -> str:
        pass  # return encrypted data

    def decrypt_data(self, data) -> str:
        pass  # return decrypted data

    def read_data(self):
        data = self.wrappee.read_data()
        return self.decrypt_data(data)


class CompressionDecorator(DataSourceDecorator):

    def write_data(self, data):
        compressed_data = self.compress_data(data)
        self.wrappee.write_data(compressed_data)

    def compress_data(self, data) -> str:
        pass  # return compressed data

    def decompress_data(self, data) -> str:
        pass  # return decompressed data

    def read_data(self):
        data = self.wrappee.read_data()
        return self.decompress_data(data)


def create_data_source(enabled_encryption: bool, enabled_compression: bool):
    source = FileDataSource("source")
    if enabled_encryption:
        source = EncryptionDecorator(source)
    if enabled_compression:
        source = CompressionDecorator(source)
    return source
