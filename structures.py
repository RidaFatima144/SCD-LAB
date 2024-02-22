class DataProcessor:
    def _init_(self):
        pass

    def sort_tuple(self, data):
        return tuple(sorted(data))

    def append_list(self, data, element):
        data.append(element)
        return data

    def update_dictionary(self, data, key, value):
        data[key] = value
        return data

    def remove_from_set(self, data, element):
        data.discard(element)
        return data


    # Creating an instance of DataProcessor
    data_processor = DataProcessor()

    # Testing sort_tuple method
    tuple_data = (5, 2, 8, 1, 3)
    sorted_tuple = data_processor.sort_tuple(tuple_data)
    print("Sorted Tuple:", sorted_tuple)

    # Testing append_list method
    list_data = [10, 20, 30]
    appended_list = data_processor.append_list(list_data, 40)
    print("Appended List:", appended_list)

    # Testing update_dictionary method
    dict_data = {'a': 1, 'b': 2, 'c': 3}
    updated_dict = data_processor.update_dictionary(dict_data, 'd', 4)
    print("Updated Dictionary:", updated_dict)

    # Testing remove_from_set method
    set_data = {1, 2, 3, 4, 5}
    removed_set = data_processor.remove_from_set(set_data, 3)
    print("Set with Element Removed:", removed_set)
