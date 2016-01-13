
class CsvExporter():
    def __init__(self, filename, columns):
        self.filename=filename
        self.columns = columns
        self.f = open(filename,'w')
        for column in self.columns:
            self.f.write(column+"\t")
        self.f.write("\n")

    def write_row(self,row):
        for column in self.columns:
            try:
                self.f.write(str(row[column])+'\t')
            except:
                self.f.write("NA\t")
        self.f.write("\n")


