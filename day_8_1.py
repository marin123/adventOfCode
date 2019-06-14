def parse_input(input_data, metadata_total):
    if len(input_data) > 0:
        child_no = int(input_data[0])
        metadata_no = int(input_data[1])
        if child_no > 0:
            if metadata_no > 0:
                metadata = input_data[-metadata_no:]
                metadata_total = metadata_total + sum(metadata)
                new_input = input_data[2:len(input_data) - metadata_no]
            else:
                metadata = []

        else:
            metadata = input_data[2:2+metadata_no]
            new_input = input_data[2+metadata_no:]
            metadata_total += sum(metadata)
        print(child_no, metadata_no, metadata, input_data)
        return parse_input(new_input, metadata_total)
    else:
        return metadata_total

f = open("input_day_8_test.txt", "r")
file_input = f.readline().split()
file_input = list(map(int, file_input))
print(parse_input(file_input, 0))
