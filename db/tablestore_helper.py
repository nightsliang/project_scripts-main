# -*- coding: utf8 -*-

"""table_store数据操作"""
import time

from tablestore import *
from tablestore import WriteRetryPolicy


class Tablestore(object):

    def __init__(self):
        # 初始化tablestore客户端
        self.client = OTSClient('https://weyes.cn-hongkong.ots.aliyuncs.com', 'LTAIJ1WLZ4lLC2nT',
                                'Gi710L7AaDeU5vFrokhBaw9p2vOzcd', 'weyes', logger_name='weyes.log',
                                retry_policy=WriteRetryPolicy())

        print("初始化成功")

    def create_table(self, table_name, schema_of_primary_key):
        """
        schema_of_primary_key = [('gid', 'INTEGER'), ('uid', 'STRING')]
        """
        table_meta = TableMeta(table_name, schema_of_primary_key)
        table_options = TableOptions()
        reserved_throughput = ReservedThroughput(CapacityUnit(0, 0))

        self.client.create_table(table_meta, table_options, reserved_throughput)
        print('tablestore表格%s创建成功' % table_name)
        time.sleep(3)

    def delete_table(self, table_name):
        self.client.delete_table(table_name)
        print('表格 \'%s\'删除成功' % table_name)

    def get_row(self, table_name, primary_key, columns_to_get):
        """
        # 目标数据的主键
        primary_key = [('gid', 1), ('uid', '101')]
        # 待获取目标字段
        columns_to_get = ['name', 'address', 'age','counter']

        """
        consumed, return_row, next_token = self.client.get_row(table_name, primary_key, columns_to_get, None, 1)
        print('Read succeed, consume %s read cu.' % consumed.read)
        print('Value of attribute: %s' % return_row.attribute_columns)
        return consumed, return_row, next_token

    def get_rows(self, table_name, indexes, bool_query, count=1, sort=Sort(sorters=[FieldSort('update_time', SortOrder.DESC)])):
        """
        # 获取多条数据,
        # 查询条件设置,customs_status字段不存在的数据
        bool_query = BoolQuery(must_not_queries=[ExistsQuery('customs_status')])
        # 查询数据
        table_name = "facebook_main"
        indexes = "resource"

        """
        rows, next_token, total_count, is_all_succeed = self.client.search(
            table_name, indexes,
            SearchQuery(bool_query, sort=sort,limit=count, get_total_count=True),
            ColumnsToGet(return_type=ColumnReturnType.ALL)
        )
        print("待消耗数据总量：", total_count)
        print("tablestore读取到的数据长度：", rows)
        return rows, next_token, total_count, is_all_succeed

    def put_row(self, table_name, primary_key, **kwargs):
        """
        # 设置主键值
        primary_key = [('gid', 1), ('uid', "101")]
        # 设置字段及字段值
        attribute_columns = [('name', 'John'), ('mobile', 15100000000), ('address', 'China'), ('age', 20)]

        """
        try:
            attribute_columns = list(kwargs.items())
            # 生成完整的数据
            row = Row(primary_key, attribute_columns)
            # 设置添加数据的条件
            # Expect not exist: put it into table only when this row is not exist.
            condition = Condition(RowExistenceExpectation.IGNORE)
            # 添加数据
            consumed, return_row = self.client.put_row(table_name, row, condition)
            print("数据添加成功")
            return True
        except:
            print("数据添加失败")
            return False

    def update_row(self, table_name, primary_key, update_of_attribute_columns, condition):
        """
        数据满足形式，示例
        primary_key = [('gid', 1), ('uid', "101")]
        update_of_attribute_columns = {
             # 修改数据
            'PUT': [('name', 'David'), ('address', 'Hongkong')],
             # 删除数据
            'DELETE': [('address', None, 1488436949003)],
            'DELETE_ALL': [('mobile'), ('age')],
             # 新增字段
            'INCREMENT': [('counter', -1)]
        }
        # 满足的别的条件 # update row only when this row is exist
        condition = Condition(RowExistenceExpectation.IGNORE, SingleColumnCondition("age", 20, ComparatorType.EQUAL))

        # 原始数据[('name', 'John'), ('mobile', 15100000000), ('address', 'China'), ('age', 20)]
        # 读取到的数据：[('address', 'China', 1569308290787), ('age', 20, 1569308290787), ('name', 'John', 1569308290787)]
        # 修改后的数据：[('address', 'Hongkong', 1569308290841), ('counter', -1, 1569308290841), ('name', 'David', 1569308290841)]
        """
        primary_key = primary_key
        update_of_attribute_columns = update_of_attribute_columns
        row = Row(primary_key, update_of_attribute_columns)
        condition = condition  # update row only when this row is exist
        consumed, return_row = self.client.update_row(table_name, row, condition)
        print('Update succeed, consume %s write cu.' % consumed.write)
        print(consumed, return_row)


if __name__ == '__main__':
    runner = Tablestore()
    schema_of_primary_key = [('gid', 'INTEGER'), ('uid', 'STRING')]
    # runner.delete_table(table_name)
    # runner.get_rows(bool_query)
