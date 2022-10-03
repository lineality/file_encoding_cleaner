"""
Multi-Step encodeing cleaner

Step 1: Try known encodings
Step 2: Disregard Errors

"""
name_of_your_file = input("Name your file here: \n")

cleaed_file_name = "cleaned_utf8_" + name_of_your_file


codecs = ['ascii','big5','big5hkscs','cp037','cp273','cp424','cp437','cp500','cp720','cp737','cp775','cp850','cp852','cp855',
          'cp856','cp857','cp858','cp860','cp861','cp862','cp863','cp864','cp865','cp866','cp869','cp874','cp875','cp932','cp949',
          'cp950','cp1006','cp1026','cp1125','cp1140','cp1250','cp1251','cp1252','cp1253','cp1254','cp1255','cp1256','cp1257','cp1258',
          'euc_jp','euc_jis_2004','euc_jisx0213','euc_kr','gb2312','gbk','gb18030','hz','iso2022_jp','iso2022_jp_1','iso2022_jp_2',
          'iso2022_jp_2004','iso2022_jp_3','iso2022_jp_ext','iso2022_kr','latin_1','iso8859_2','iso8859_3','iso8859_4','iso8859_5','iso8859_6',
          'iso8859_7','iso8859_8','iso8859_9','iso8859_10','iso8859_11','iso8859_13','iso8859_14','iso8859_15','iso8859_16','johab','koi8_r','koi8_t',
          'koi8_u','kz1048','mac_cyrillic','mac_greek','mac_iceland','mac_latin2','mac_roman','mac_turkish','ptcp154','shift_jis','shift_jis_2004',
          'shift_jisx0213','utf_32','utf_32_be','utf_32_le','utf_16','utf_16_be','utf_16_le','utf_7','utf_8','utf_8_sig']

stop_flag = False


try:
    
    for x in range(len(codecs)):
        if stop_flag == False:
            print(x,': Now checking use of:', codecs[x])
        
            try:
                # read it
                with open( name_of_your_file, "r", errors='ignore') as file_object:
                    # read file content
                    data = file_object.read()
                    
                stop_flag == True

                # make it
                with open( cleaed_file_name, "w", encoding='utf-8') as file_object2:
                    # write file content
                    file_object2.write( data )
                
                print(codecs[x], ' Worked!! ', codecs[x], '\n')  
                print("clean File Made: OK!")
                break
                
            except:
                print(codecs[x], ' did NOT work. Moving on...', codecs[x], '\n')

        print("stop_flag", stop_flag)

except:

    # read it
    with open( name_of_your_file, "r", errors='ignore') as file_object:
        # read file content
        data = file_object.read()


    # make it
    with open( cleaed_file_name, "w", encoding='utf-8') as file_object:
        # write file content
        file_object.write( data )

    print("clean File Made: OK!")
