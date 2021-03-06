import DataClass as dc
import DataCleaning.MissingDataHandle as mdh
import DataCleaning.OutlierHandle as oh

if __name__ == "__main__":
    data = dc.DataClass([str] + [float] * 12)
    data.read(r"E:\_Python\DataPreprocessing\sample\fz_micro.txt", False)
    data.parse()
    mdh.mid_interpolation_handle(data, [i for i in range(1, 13)])
    oh.outlier_none_handle(data, [i for i in range(1, 13)], "z_score", 3.0)
    print(data.data)