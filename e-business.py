customer_number=[40686,49827,37819,10537,73905,18383,27407,78736,18765,90299,58005,88390,20056,14099,56315,17539,29251,14884,20717,26589,21898,93596,83844,53750,49492,51727,99788,44901,48969,63850]
customer_name=["Carey, Drew Allison","Butler, Geoffrey Barbara","Burkhart, Jackie Beulah","Sheffield, Maxwell B","Deveraux, Blanche E","Ricardo, Lucy Esmeralda","Mosby, Ted Evelyn","Montgomery, Dharma F","Addams, Wednesday Friday","Scott, Michael Gary","Fonzarelli, Arthur H","Torres, Callie Iphigenia","Simpson, Bart Jojo","Sisko, Benjamin L","Hofstadter, Leonard L","Norton, Edward Lilywhite","Costanza, George Louis","Griffin, Peter Lowenbrau","Burns, Frank Marion","Lemon, Liz Miervaldis","Bing, Chadler Muriel","Keaton, Alex P","Petrie, Ritchie Rosebud","Hennessey, Cate Stinky","Boyd, Woody Tiberius","Carter, John Truman","Douglass, Oliver Wendell","Feeney, Shirley Wilhemina","Mulder, Fox William","Crane, Frasier Winslow"]
customer_balance=[301652.58,36958.5,374105.23,32202.08,331741.13,28457.42,395649.6,29726.1,1796.93,37471.83,347370.39,36620.43,34406.58,2907.09,7318.02,32680.73,17758.06,9146.31,36020.05,19911.97,14724.23,12059.91,38900.33,20447.64,26802.38,14537.16,29255.65,39782.92,30949.89,14171.2]
customer_password=["Iz9*z$","Eu7#*%","Fv6&x","Ea0#5","Tw6!b8","Ye4&","Up2%)","Rk2!F","Ig6)Dw","Dr3@J","Oi2^Wg","Co7@(","Ra4@(","Hl3#Uk8","Xu9!w#@","Nf0&","Wd9(","Gh7*Op","Mf2#D$","Oj9@&","Ha3$","Oz6^%","Lr7@E","Bj2#7*","Pz3!","Go1(","Fe8(k*","Jb4)%","Ue4&","Qy2&w("]
item_number=["K733","LO917","L223","O261","NQ813","TH851","YJ467","UN941","WR893","SD743","IL993","L761","NO204","GO642","BC571","TX31","NG108","AF977","SA868","A411","YJ195","YC871","NN896","D636","K233","BM608","L982","UO399","Y337","T397"]
item_description=["Pens","Pencils","Markers","Highlighters","Paper clips","Tape","Rubber bands","Erasers","Stamp pads","Ink for stamp pads","Spiral notebooks","Writing pads","Post–it® notes","Phone message pads","Laser printer paper","Copy paper","Fax paper","Graph paper","Colored paper","Pocket notebook","Manila file folders","Hanging file folders","Pocket folders","File labels","Index dividers","Tabs","Letter envelopes","Catalog envelopes","Padded envelopes","Shipping paper"]
item_price=[12.88,2.83,30.38,82.93,99.64,68.81,96.08,55.55,9.06,40.42,23.08,58.72,18.77,27.43,20.17,67.91,39.33,81.6,60.94,44.16,55.5,52.09,94.17,67.89,46.67,15.33,81.83,63.26,11.9,27.05]

import re 
import string

request=input('')

if request[:2] != 'NC' and request[:2] != 'NP' and request[:2] != 'CO':
    print('Transaction type',request[:2],'is invalid.')

number = int(request[2:7])  
if (number in customer_number) == False:
    print ('Customer number', request[2:7], 'is invalid.')
    
    if(request[:2] == 'NC'):
    number = int(request[2:7])  
    if (number in customer_number) == True:
        i= customer_number.index(int(request[2:7]))
        index2 = [m.start() for m in re.finditer(r" ",request)][1]
        customer_name[i] = request[index2+1:] + ', ' + request[7:index2]
        print(customer_name)

#NP10537AB2%Ce'#1   
if (request[:2] == 'NP'):
    if (len(request)<13) or (not request[7].isupper()) or (not request[8].islower()) or (not request[9].isnumeric()) or (not (request[10] in '!@#$%^&*()')):
        print('New password not secure. Request denied.')
   
 else:
        number = int(request[2:7])  
        if (number in customer_number) == True:
            i= customer_number.index(int(request[2:7]))
            customer_password[i] = request[7:]
            print(customer_password)
if (request[:2] == 'CO'):
    number_item = request[7]
    if (int(number_item) == 1):
        line0=input('')
#print('Order Date:     ' + request[8:10] +'/' + request[10:12] +'/' + request[12:17] )
        date3 = request[8:10] +'/' + request[10:12] +'/' + request[12:17]
        print('{:>10}'.format('Order Date:'), '{:>14}'.format(date3))
        number = int(request[2:7])
        if (number in customer_number) == True:
            i= customer_number.index(int(request[2:7]))
            lc= request[2:7]
            tc=customer_name[i]
            print('{:>11}'.format('Customer:'), '{:>14}'.format(lc), '{:>29}'.format(tc)+ '\n')  
            
            print('{:^3}'.format('Ln#')+'   ' + '{:18}'.format('Item #')+ '{:28}'.format('Item Description')+ '{:^10}'.format('Req Date')+  '{:>11}'.format('Qty'), '{:>10}'.format('Price'), '{:>13}'.format('Total'))
            indexspecial= line0.find('^')
            indexsecond = len(line0) - 8
            item = line0[indexspecial+1 : indexsecond -1]
            quality = line0[:indexspecial]
            date = line0[indexsecond:]
            i= item_number.index(item)
            
            total_price = float(quality) * item_price[i]
            describe = item_description[i]
            total_priceround = round(total_price, 2)
            lc= date[0:2]+'/'+date[2:4]+'/'+date[4:]
            ldf =item_price[i]
            #print('{:^3}'.format('Ln#')+'   ' + '{:18}'.format('Item #')+ '{:28}'.format('Item Description')+ '{:^10}'.format('Req Date')+  '{:>11}'.format('Qty'), '{:>10}'.format(ldf), '{:>13}'.format('Total'))
            print(' 1   ', '{:17}'.format(item), '{:27}'.format(describe) , '{:^10}'.format(lc) ,  '{:>10}'.format(quality),  '{:>10}'.format(ldf), '  $', '{:>9}'.format("%.2f" % total_priceround)+'\n')   
            print('                                                                           Total', '{:>17}'.format("%.2f" % total_priceround))
            
if (int(number_item) == 2):
        line0=input('')
        line1=input('')
        date3 = request[8:10] +'/' + request[10:12] +'/' + request[12:17]
        print('{:>10}'.format('Order Date:'), '{:>14}'.format(date3))
        number = int(request[2:7])
        if (number in customer_number) == True:
i= customer_number.index(int(request[2:7]))
            lc= request[2:7]
            tc=customer_name[i]
            print('{:>11}'.format('Customer:'), '{:>14}'.format(lc), '{:>29}'.format(tc)+ '\n')
            #bhl line 59
            print('{:^3}'.format('Ln#')+'   ' + '{:18}'.format('Item #')+ '{:28}'.format('Item Description')+ '{:^10}'.format('Req Date')+  '{:>11}'.format('Qty'), '{:>10}'.format('Price'), '{:>13}'.format('Total'))
            #print('  Customer:          ' + request[2:7] + '           '+  customer_name[i]+'\n')
            #print('Ln#   Item #            Item Description             Req Date         Qty      Price         Total')
            indexspecial= line0.find('^')
            indexsecond = len(line0) - 8
            item = line0[indexspecial+1 : indexsecond -1]
            quality = line0[:indexspecial]
            date = line0[indexsecond:]
            t= item_number.index(item)
            total_price = float(quality) * item_price[t]
            describe = item_description[t]
            total_priceround = round(total_price, 2)
            
            lc= date[0:2]+'/'+date[2:4]+'/'+date[4:]
            ldf =item_price[t]
            
            #print(' 1    '+ item + '             '+ describe + '                     '+ date[0:2]+'/'+date[2:4]+'/'+date[4:] + '        '+ quality + '      ', item_price[t], '  $   ', "%.2f"%total_priceround)
            print(' 1   ', '{:17}'.format(item), '{:27}'.format(describe) , '{:^10}'.format(lc) ,  '{:>10}'.format(quality),  '{:>10}'.format(ldf), '  $', '{:>9}'.format("%.2f" % total_priceround))   
            
            indexspecial2= line1.find('^')
            indexsecond2 = len(line1) - 8
            item2 = line1[indexspecial2+1 : indexsecond2 -1]
            quality2 = line1[:indexspecial2]
            date2 = line1[indexsecond2:]
            t2= item_number.index(item2)
            describe2 = item_description[t2]
            total_price2 = float(quality2) * item_price[t2]
            total_priceround2 = round(total_price2, 2)
            
            lc2= date2[0:2]+'/'+date2[2:4]+'/'+date2[4:]
            ldf2 =item_price[t2]     
            #print(' 2    '+ item2 + '              '+ describe2 + '              ' + date2[0:2]+'/'+date2[2:4]+'/'+date2[4:] + '      '+ quality2 + '     ', item_price[t2], '  $'+"%.2f"%total_priceround2+'\n')
            print(' 2   ', '{:17}'.format(item2), '{:27}'.format(describe2) , '{:^10}'.format(lc2) ,  '{:>10}'.format(quality2),  '{:>10}'.format(ldf2), '  $'+ '{:>9}'.format("%.2f"%total_priceround2)+ '\n')   #"%.2f" % a
                        
            total = total_priceround + total_priceround2
            
            #print('                                                                           Total       ', "%.2f"%total)
            print('                                                                           Total', '{:>17}'.format("%.2f" % total))
            
