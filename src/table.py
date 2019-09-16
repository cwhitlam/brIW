class Table:
    def __init__(self, table_title, object_attributes, table_contents, column_names = [], column_widths = []): 
        self.table_title       = table_title
        self.table_contents    = table_contents.values() if isinstance(table_contents, dict) else table_contents
        self.object_attributes = object_attributes 

        #Used to set custom column names that are different to the class attributes.
        #Must be the same number of column names as class variables being displayed
        #If no column names entered, will default to using class attributes at column titles
        if (column_names == []):
            self.column_names = object_attributes
        else:
            self.column_names = column_names

        #Can be used to set custom widths per column.
        #Highly untested and not recommended
        if (column_widths == []):
            self.column_widths = self.calculate_column_widths()
        else:
            self.column_widths = column_widths

    def calculate_table_width(self):
        num_of_columns = len(self.object_attributes)
        return (2*num_of_columns + sum(self.column_widths)) +1

    def calculate_column_widths(self):
        column_widths = []
        
        for index in range(0, len(self.column_names)):
            column_width = len(self.column_names[index])
            for row in self.table_contents:
                cell_text = getattr(row, self.object_attributes[index])
                cell_text_length = len(str(cell_text))
                if (cell_text_length > column_width):
                    column_width = cell_text_length
            column_width += 1 #Add one for extra space at end of each cell
            column_widths.append(column_width)
        return column_widths

    def print_table_header(self, table_width):
        print(self.table_title.upper())
        seperator = "+" + "="*(table_width-2) + "+"
        print(seperator)
        titles = ""
        for index in range(0, len(self.object_attributes)):
            padding_amount = self.column_widths[index] - len(str(self.column_names[index]))
            titles += "| " + self.column_names[index].upper() + (" "*padding_amount)
        print(titles + "|")
        print(seperator)

    def print_table_contents(self):
        for row in self.table_contents:
            row_text = ""
            for index in range(0, len(self.object_attributes)):
                cell_text = str(getattr(row, self.object_attributes[index]))
                padding_amount = self.column_widths[index] - len(cell_text)
                row_text += "| " + cell_text + (" "*padding_amount)
            print(row_text + "|")

    def print_table(self):
        table_width = self.calculate_table_width()
        self.print_table_header(table_width)
        self.print_table_contents()
        print("+" + "="*(table_width-2) +"+\n")
