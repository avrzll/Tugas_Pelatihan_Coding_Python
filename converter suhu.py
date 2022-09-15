def convertsuhu():
    print ('\n<<< SELAMAT DATANG DI PROGRAM KONVERSI SUHU >>>')
    print ('\n---PILIH SALAH SATU---')
    print ('[a.] Konversi suhu Celcius (C)')
    print ('[b.] Konversi suhu Fahrenheit (F)')
    print ('[c.] Konversi suhu Kelvin (K)')
    print ('[d.] Konversi suhu Reamur (R)')
    choice_menu = input('Pilih (a, b, c, or d) = ')

    '''
    KONVERSI SUHU DARI CELCIUS KE FAHRENHEIT, KELVIN, REAMUR
    '''

    if (choice_menu == 'a'):
        print ('\nKONVERSI SUHU CELCIUS (C)')
        print ('[1.]Celcius to Fahrenheit')
        print ('[2.]Celcius to Kelvin')
        print ('[3.]Celcius to Reamur')
        choice_submenu_celcius = int(input('Pilih (1, 2, or 3) = '))

        #CELCIUS KE FAHRENHEIT
        if (choice_submenu_celcius == 1):
            print ('\nKonversi Celcius ke Fahrenheit')
            celcius = int(input('Masukkan suhu : '))
            fahrenheit = celcius * (9/5) + 32
            print("Suhu dalam fahrenheit adalah = {} F".format(fahrenheit))

        #CELCIUS KE KELVIN
        elif (choice_submenu_celcius == 2):
            print ('\nKonversi Celcius ke Kelvin')
            celcius = int(input('Masukkan suhu : '))
            kelvin = celcius + 273.15
            print("suhu dalam kelvin adalah = {} K".format (kelvin))

        #CELCIUS KE REAMUR
        elif (choice_submenu_celcius == 3):
            print ('\nKonversi Celcius ke Reamur')
            celcius = int(input('Masukkan suhu : '))
            reamur = celcius * (4/5)
            print("Suhu dalam reamur adalah = {} R".format (reamur))

        '''
        KONVERSI SUHU DARI FAHRENHEIT KE CELCIUS, KELVIN, REAMUR
        '''

    elif (choice_menu == 'b'):
        print ('\nKONVERSI SUHU FAHRENHEIT (F)')
        print ('[1.]Fahrenheit to Celcius')
        print ('[2.]Fahrenheit to Kelvin')
        print ('[3.]Fahrenheit to Reamur')
        choice_submenu_fahrenheit = int(input('Pilih (1, 2, or 3) = '))

        #FAHRENHEIT KE CELCIUS
        if (choice_submenu_fahrenheit == 1):
            print ('\nKonversi Fahrenheit ke Celcius')
            fahrenheit = int(input('Masukkan suhu : '))
            celcius = (fahrenheit - 32) * 5/9
            print("Suhu dalam celcius adalah = {} C".format(celcius))

        #FAHRENHEIT KE KELVIN
        elif (choice_submenu_fahrenheit == 2):
            print ('\nKonversi Fahrenheit ke Kelvin')
            fahrenheit = int(input('Masukkan suhu : '))
            kelvin = (fahrenheit + 459.67) * 5/9
            print("Suhu dalam kelvin adalah = {} K".format (kelvin))

        #FAHRENHEIT KE REAMUR
        elif (choice_submenu_fahrenheit == 3):
            print ('\nKonversi Fahrenheit ke Reamur')
            fahrenheit = int(input('Masukkan suhu : '))
            reamur = 4/9 * (fahrenheit - 32)
            print("suhu dalam reamur adalah = {} R".format (reamur))


        '''
        KONVERSI SUHU DARI KELVIN KE CELCIUS, FAHRENHEIT, REAMUR
        '''

    elif (choice_menu == 'c'):
        print ('\nKONVERSI SUHU KELVIN (K)')
        print ('[1.]Kelvin to Celcius')
        print ('[2.]Kelvin to Fahrenheit')
        print ('[3.]Kelvin to Reamur')
        choice_submenu_kelvin = int(input('Pilih (1, 2, or 3) = '))

        #KELVIN KE CELCIUS
        if (choice_submenu_kelvin == 1):
            print ('\nKonversi Kelvin ke Celcius')
            kelvin = int(input('Masukkan suhu : '))
            celcius = kelvin - 273.15
            print("Suhu dalam celcius adalah = {} C".format(celcius))

        #KELVIN KE FAHRENHEIT
        elif (choice_submenu_kelvin == 2):
            print ('\nKonversi Kelvin ke Fahrenheit')
            kelvin = int(input('Masukkan suhu : '))
            fahrenheit = (kelvin * 9/5) - 459.67
            print("Suhu dalam fahrenheit adalah = {} F".format (fahrenheit))

        #KELVIN KE REAMUR
        elif (choice_submenu_kelvin == 3):
            print ('\nKonversi Kelvin ke Reamur')
            kelvin = int(input('Masukkan suhu : '))
            reamur = 4/5 * (kelvin - 273)
            print("Suhu dalam reamur adalah = {} R".format (reamur))

        '''
        KONVERSI SUHU DARI REAMUR KE CELCIUS, FAHRENHEIT, KELVIN
        '''

    elif (choice_menu == 'd'):
        print ('\nKONVERSI SUHU REAMUR (R)')
        print ('[1.]Reamur to Celcius')
        print ('[2.]Reamur to Fahrenheit')
        print ('[3.]Reamur to Kelvin')
        choice_submenu_reamur = int(input('Pilih (1, 2, or 3) = '))

        #REAMUR KE CELCIUS
        if (choice_submenu_reamur == 1):
            print ('\nKonversi Reamur ke Celcius')
            reamur = int(input('Masukkan suhu : '))
            celcius = reamur / 0.8
            print("Suhu dalam celcius adalah = {} C".format(celcius))

        #REAMUR KE FAHRENHEIT
        elif (choice_submenu_reamur == 2):
            print ('\nKonversi Reamur ke Fahrenheit')
            reamur = int(input('Masukkan suhu : '))
            fahrenheit = ( reamur * 2.25 ) + 32
            print("Suhu dalam fahrenheit adalah = {} F".format (fahrenheit))

        #REAMUR KE KELVIN
        elif (choice_submenu_reamur == 3):
            print ('\nKonversi Reamur ke Kelvin')
            reamur = int(input('Masukkan suhu : '))
            kelvin = ( reamur / 0.8 ) + 273.15
            print("Suhu dalam kelvin adalah = {} K".format (kelvin))

    input('\nPress enter to continue...')
    print('\nMau convert lagi ?')
    print('[1.] Iya')
    print('[2.] Tidak')
    convert_lagi = int(input('Input 1 jika "iya" atau Input 2 jika "tidak" => '))
    if (convert_lagi == 1):
        convertsuhu()
    
    elif (convert_lagi) == 2:
        print('\n<<< TERIMAKASIH TELAH MENGGUNAKAN PROGRAM SAYA >>>\n')

convertsuhu()
