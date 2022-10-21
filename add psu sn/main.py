

def main():
    file = "D:/user_data/Martin/OneDrive - Straumann Group/DHF/100 Verification & Validation/101 Verification/Hardware/New Power Supply/Log New Power Supply/Data_summary.csv"
    file_to_write = "D:/user_data/Martin/OneDrive - Straumann Group/DHF/100 Verification & Validation/101 Verification/Hardware/New Power Supply/Log New Power Supply/Data_summary_test.csv"
    to_write = []
    sn_list = ["PSU,SC195A1881,", "PSU,SC195A1882,", "PSU,SC195A1883,", "PSU,SC195A1884,", "PSU,SC195A1885,",
               "PSU,SC195A1886,", "PSU,SC195A1887,", "PSU,SC195A1888,", "PSU,SC195A1889,", "PSU,SC195A1890,",
               "PSU,SC195A1891,", "PSU,SC195A1892,", "PSU,SC195A1893,", "PSU,SC195A1894,", "PSU,SC195A1895,",
               "PSU,SC195A1896,", "PSU,SC195A1897,", "PSU,SC195A1898,", "PSU,SC195A1899,", "PSU,SC195A1900,",
               "PSU,SC195A1901,", "PSU,SC195A1902,", "PSU,SC195A1903,", "PSU,SC195A1904,", "PSU,SC195A1905,",
               "PSU,SC195A1906,", "PSU,SC195A1907,", "PSU,SC195A1908,", "PSU,SC195A1909,", "PSU,SC195A1910,",
               "PSU,SC195A1911,", "PSU,SC195A1912,", "PSU,SC195A1913,", "PSU,SC195A1914,", "PSU,SC195A1915,",
               "PSU,SC195A1916,", "PSU,SC195A1917,", "PSU,SC195A1918,", "PSU,SC195A1919,", "PSU,SC195A1920,",
               "PSU,SC195A1921,", "PSU,SC195A1922,", "PSU,SC195A1923,", "PSU,SC195A1924,", "PSU,SC195A1925,",
               "PSU,SC195A1926,", "PSU,SC195A1927,", "PSU,SC195A1928,", "PSU,SC195A1929,", "PSU,SC195A1930,",
               "PSU,SC195A1931,", "PSU,SC195A1932,", "PSU,SC195A1933,", "PSU,SC195A1934,", "PSU,SC195A1935,",
               "PSU,SC195A1936,", "PSU,SC195A1937,", "PSU,SC195A1938,", "PSU,SC195A1939,", "PSU,SC195A1940,"]
    counter = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if "hp serial" in line:
                to_write.append(sn_list[counter] + "\n")
                to_write.append(line)
                counter += 1
            else:
                to_write.append(line)

    with open(file_to_write, 'w') as fw:
        for lines in to_write:
            fw.writelines(lines)



if __name__ == '__main__':
    main()

