sample_data = [
    {'id': 1, 'name': 'Alice', 'age': 30},
    {'id': 2, 'name': 'Bob', 'age': 25},
    {'id': 3, 'name': 'Charlie', 'age': 35}
]
chart_data={
      'time': ['09:15', '09:20', '09:25', '09:30', '09:35', '09:40', '09:45', '09:50', '09:55', '10:00', '10:05', '10:10', '10:15', '10:20', '10:25', '10:30', '10:35', '10:40', '10:45', '10:50', '10:55', '11:00', '11:05', '11:10', '11:15', '11:20', '11:25', '11:30', '11:35', '11:40', '11:45', '11:50', '11:55', '12:00', '12:05', '12:10', '12:15', '12:20', '12:25', '12:30', '12:35', '12:40', '12:45', '12:50', '12:55', '13:00', '13:05', '13:10', '13:15', '13:20', '13:25', '13:30', '13:35', '13:40', '13:45', '13:50', '13:55', '14:00', '14:05', '14:10', '14:15', '14:20', '14:25', '14:30', '14:35', '14:40', '14:45', '14:50', '14:55', '15:00', '15:05', '15:10', '15:15', '15:20', '15:25'], 
      'NIFTY50': [22491, 22498, 22511, 22515, 22501, 22488, 22460, 22454, 22454, 22465, 22481, 22481, 22515, 22518, 22529, 22539, 22536, 22528, 22522, 22523, 22528, 22525, 22536, 22537, 22543, 22541, 22538, 22534, 22531, 22540, 22546, 22544, 22554, 22559, 22566, 22559, 22560, 22571, 22570, 22567, 22564, 22571, 22567, 22572, 22573, 22570, 22577, 22576, 22577, 22592, 22599, 22607, 22612, 22619, 22608, 22608, 22621, 22617, 22607, 22611, 22617, 22623, 22614, 22617, 22626, 22608, 22608, 22627, 22628, 22639, 22649, 22653, 22647, 22640, 22633], 
      'SENSEX': [74013, 74069, 74161, 74162, 74122, 74095, 74014, 73980, 73987, 74039, 74118, 74104, 74216, 74221, 74259, 74281, 74268, 74245, 74223, 74211, 74250, 74243, 74292, 74290, 74314, 74304, 74291, 74270, 74281, 74303, 74329, 74310, 74362, 74381, 74404, 74368, 74369, 74411, 74408, 74392, 74387, 74411, 74411, 74414, 74427, 74416, 74426, 74424, 74421, 74476, 74514, 74548, 74576, 74607, 74564, 74556, 74611, 74589, 74569, 74582, 74598, 74622, 74560, 74593, 74621, 74557, 74568, 74648, 74646, 74676, 74701, 74717, 74702, 74690, 74671], 
      'BANK-NIFTY': [48406, 48504, 48574, 48530, 48541, 48511, 48442, 48437, 48408, 48433, 48544, 48552, 48654, 48690, 48696, 48757, 48756, 48714, 48710, 48703, 48702, 48684, 48717, 48721, 48822, 48818, 48810, 48804, 48799, 48862, 48875, 48873, 48916, 48920, 48951, 48952, 48939, 48971, 48966, 48928, 48955, 49018, 48998, 49004, 49009, 48987, 49001, 48997, 49014, 49068, 49158, 49210, 49282, 49335, 49300, 49315, 49379, 49360, 49330, 49348, 49330, 49324, 49285, 49325, 49349, 49310, 49335, 49416, 49424, 49403, 49460, 49462, 49442, 49386, 49381], 
      'NIFTY-IT': [33744, 33734, 33677, 33697, 33687, 33650, 33624, 33579, 33595, 33592, 33576, 33563, 33606, 33572, 33599, 33588, 33578, 33566, 33587, 33598, 33604, 33658, 33657, 33648, 33610, 33615, 33616, 33599, 33625, 33618, 33630, 33626, 33629, 33611, 33620, 33628, 33621, 33650, 33640, 33645, 33616, 33610, 33620, 33620, 33643, 33677, 33662, 33632, 33636, 33624, 33615, 33611, 33623, 33605, 33592, 33581, 33588, 33602, 33586, 33581, 33587, 33575, 33571, 33575, 33579, 33540, 33547, 33533, 33548, 33577, 33576, 33590, 33584, 33580, 33571], 
      'NIFTY-FINANCE': [11030, 11027, 11025, 11028, 11023, 11017, 11012, 11017, 11018, 11016, 11022, 11022, 11021, 11021, 11026, 11025, 11024, 11023, 11026, 11027, 11025, 11023, 11027, 11023, 11024, 11023, 11022, 11027, 11027, 11024, 11028, 11031, 11037, 11036, 11036, 11037, 11041, 11040, 11039, 11042, 11042, 11038, 11034, 11034, 11035, 11037, 11038, 11033, 11032, 11031, 11030, 11031, 11030, 11031, 11031, 11036, 11041, 11037, 11035, 11040, 11045, 11042, 11039, 11043, 11028, 11030, 11032, 11036, 11034, 11040, 11041, 11042, 11047, 11043], 
      'NIFTY-ENERGY': [19082, 19110, 19091, 19095, 19126, 19118, 19077, 19073, 19071, 19051, 19061, 19057, 19071, 19081, 19099, 19103, 19111, 19095, 19082, 19076, 19066, 19064, 19069, 19065, 19067, 19078, 19079, 19092, 19091, 19079, 19076, 19071, 19091, 19098, 19078, 19081, 19072, 19082, 19089, 19088, 19084, 19084, 19080, 19079, 19084, 19099, 19130, 19135, 19148, 19144, 19123, 19117, 19098, 19092, 19096, 19102, 19098, 19108, 19088, 19066, 19048, 19073, 19047, 19035, 19036, 19011, 19016, 19028, 19038, 19077, 19098, 19103, 19106, 19109, 19099, 19099, 19122, 19117]
    }

sample_data1 = [
    {'id': 4, 'name': 'Alice', 'age': 3},
    {'id': 5, 'name': 'Bob', 'age': 2},
    {'id': 6, 'name': 'Charlie', 'age': 5}
]
datain={
  "gain": [
    {
      "Contribution": 28.53396757336203,
      "Name": "HDFCBANK.NS",
      "change": 1.601232748224581,
      "close": 1516.5
    },
    {
      "Contribution": 5.7637422218987835,
      "Name": "BHARTIARTL.NS",
      "change": 1.1244132309595753,
      "close": 1389.5
    },
    {
      "Contribution": 1.133214920071048,
      "Name": "BPCL.NS",
      "change": 1.1197775890030117,
      "close": 654.7
    },
    {
      "Contribution": 5.985295922351745,
      "Name": "LT.NS",
      "change": 0.9929157137278939,
      "close": 3621.0
    },
    {
      "Contribution": 1.48820411975814,
      "Name": "ULTRACEMCO.NS",
      "change": 0.663192566737139,
      "close": 10237.95
    },
    {
      "Contribution": 3.7361767860974258,
      "Name": "AXISBANK.NS",
      "change": 0.6608024029178327,
      "close": 1172.95
    },
    {
      "Contribution": 1.2870265914584944,
      "Name": "NTPC.NS",
      "change": 0.5909213000268569,
      "close": 374.5
    },
    {
      "Contribution": 0.6430122662376758,
      "Name": "COALINDIA.NS",
      "change": 0.5730947114417788,
      "close": 500.15
    },
    {
      "Contribution": 0.6064353936346522,
      "Name": "EICHERMOT.NS",
      "change": 0.5625560237798257,
      "close": 4880.15
    },
    {
      "Contribution": 1.5180797686878051,
      "Name": "MARUTI.NS",
      "change": 0.5036761010908444,
      "close": 13000.05
    },
    {
      "Contribution": 0.6111111111111113,
      "Name": "HINDALCO.NS",
      "change": 0.2955082742316785,
      "close": 678.8
    },
    {
      "Contribution": 0.350418155949619,
      "Name": "INDUSINDBK.NS",
      "change": 0.1873893882083524,
      "close": 1443.55
    },
    {
      "Contribution": 0.12355944566010212,
      "Name": "DIVISLAB.NS",
      "change": 0.07293946024799416,
      "close": 4116.0
    },
    {
      "Contribution": 0.04706335172281252,
      "Name": "BAJAJ-AUTO.NS",
      "change": 0.03291143477119757,
      "close": 8966.4
    },
    {
      "Contribution": 0.16421085012418749,
      "Name": "BAJFINANCE.NS",
      "change": 0.031494217515187474,
      "close": 6828.8
    }
  ],
  "gain_val": 51.99151847812563,
  "lose": [
    {
      "Contribution": -3.305906398309465,
      "Name": "ADANIPORTS.NS",
      "change": -1.8325423493954909,
      "close": 1416.9
    },
    {
      "Contribution": -2.4547430564873323,
      "Name": "TATACONSUM.NS",
      "change": -1.690594391520201,
      "close": 1099.05
    },
    {
      "Contribution": -3.27285981308412,
      "Name": "TECHM.NS",
      "change": -1.4168224299065455,
      "close": 1318.55
    },
    {
      "Contribution": -3.2584317032040473,
      "Name": "M&M.NS",
      "change": -1.2551739996933926,
      "close": 2576.45
    },
    {
      "Contribution": -2.469422028353337,
      "Name": "JSWSTEEL.NS",
      "change": -1.1941112322791763,
      "close": 906.05
    },
    {
      "Contribution": -3.5840935096537003,
      "Name": "TITAN.NS",
      "change": -1.1891484769919376,
      "close": 3411.0
    },
    {
      "Contribution": -4.986224709427465,
      "Name": "ASIANPAINT.NS",
      "change": -1.162290142057684,
      "close": 2870.0
    },
    {
      "Contribution": -11.791213448227152,
      "Name": "TCS.NS",
      "change": -1.0915768791174922,
      "close": 3850.95
    },
    {
      "Contribution": -7.249756429137889,
      "Name": "ITC.NS",
      "change": -1.0875722215928427,
      "close": 436.55
    },
    {
      "Contribution": -2.7479073547338366,
      "Name": "HCLTECH.NS",
      "change": -0.8163717631413656,
      "close": 1342.5
    },
    {
      "Contribution": -1.74115500214686,
      "Name": "WIPRO.NS",
      "change": -0.7835981107771648,
      "close": 462.15
    },
    {
      "Contribution": -0.7391199564642741,
      "Name": "HEROMOTOCO.NS",
      "change": -0.7813107362201628,
      "close": 5105.0
    },
    {
      "Contribution": -0.9686204036494288,
      "Name": "SBILIFE.NS",
      "change": -0.6773569256289712,
      "close": 1437.0
    },
    {
      "Contribution": -11.216354251562281,
      "Name": "INFY.NS",
      "change": -0.6655800054333184,
      "close": 1462.6
    },
    {
      "Contribution": -3.883126967471144,
      "Name": "HINDUNILVR.NS",
      "change": -0.6610703043022036,
      "close": 2366.75
    },
    {
      "Contribution": -0.739755545667129,
      "Name": "BRITANNIA.NS",
      "change": -0.6466394629957422,
      "close": 5247.0
    },
    {
      "Contribution": -1.5971373152297326,
      "Name": "SUNPHARMA.NS",
      "change": -0.5417697812855267,
      "close": 1487.0
    },
    {
      "Contribution": -0.7672787696898745,
      "Name": "DRREDDY.NS",
      "change": -0.5205419061668077,
      "close": 5867.0
    },
    {
      "Contribution": -2.75337098906383,
      "Name": "SBIN.NS",
      "change": -0.4927292392741285,
      "close": 828.0
    },
    {
      "Contribution": -12.47014568823382,
      "Name": "RELIANCE.NS",
      "change": -0.44076578849971093,
      "close": 2959.0
    },
    {
      "Contribution": -0.773514548862995,
      "Name": "GRASIM.NS",
      "change": -0.41364414377700265,
      "close": 2443.65
    },
    {
      "Contribution": -3.185401246306407,
      "Name": "KOTAKBANK.NS",
      "change": -0.4125098739065536,
      "close": 1702.0
    },
    {
      "Contribution": -0.8281290590741522,
      "Name": "TATAMOTORS.NS",
      "change": -0.3584974281706287,
      "close": 958.9
    },
    {
      "Contribution": -1.0304273504273407,
      "Name": "TATASTEEL.NS",
      "change": -0.3418803418803386,
      "close": 174.9
    },
    {
      "Contribution": -0.5531232948689518,
      "Name": "NESTLEIND.NS",
      "change": -0.28898813734010026,
      "close": 2467.0
    },
    {
      "Contribution": -0.4843182219086328,
      "Name": "ONGC.NS",
      "change": -0.2822367260539818,
      "close": 282.65
    },
    {
      "Contribution": -0.6079399812441144,
      "Name": "POWERGRID.NS",
      "change": -0.26570803376053953,
      "close": 319.05
    },
    {
      "Contribution": -0.5662594423202536,
      "Name": "BAJAJFINSV.NS",
      "change": -0.21449221300009605,
      "close": 1605.0
    },
    {
      "Contribution": -2.8098721903921215,
      "Name": "ICICIBANK.NS",
      "change": -0.18510356985455345,
      "close": 1132.4
    },
    {
      "Contribution": -0.24612698519289983,
      "Name": "CIPLA.NS",
      "change": -0.1645233858241309,
      "close": 1486.7
    },
    {
      "Contribution": -0.12601431980905012,
      "Name": "HDFCLIFE.NS",
      "change": -0.07955449482894578,
      "close": 565.2
    },
    {
      "Contribution": -0.0011239436855678612,
      "Name": "APOLLOHOSP.NS",
      "change": -0.0008375139236720278,
      "close": 5970.0
    }
  ],
  "neg_val": -93.2088739238892
}

dataset = {
  "ADANIPORTS.NS": -3.305906398309465,
  "APOLLOHOSP.NS": -0.0011239436855678612,
  "ASIANPAINT.NS": -4.986224709427465,
  "AXISBANK.NS": 3.7361767860974258,
  "BAJAJ-AUTO.NS": 0.04706335172281252,
  "BAJAJFINSV.NS": -0.5662594423202536,
  "BAJFINANCE.NS": 0.16421085012418749,
  "BHARTIARTL.NS": 5.7637422218987835,
  "BPCL.NS": 1.133214920071048,
  "BRITANNIA.NS": -0.739755545667129,
  "CIPLA.NS": -0.24612698519289983,
  "COALINDIA.NS": 0.6430122662376758,
  "DIVISLAB.NS": 0.12355944566010212,
  "DRREDDY.NS": -0.7672787696898745,
  "EICHERMOT.NS": 0.6064353936346522,
  "GRASIM.NS": -0.773514548862995,
  "HCLTECH.NS": -2.7479073547338366,
  "HDFCBANK.NS": 28.53396757336203,
  "HDFCLIFE.NS": -0.12601431980905012,
  "HEROMOTOCO.NS": -0.7391199564642741,
  "HINDALCO.NS": 0.6111111111111113,
  "HINDUNILVR.NS": -3.883126967471144,
  "ICICIBANK.NS": -2.8098721903921215,
  "INDUSINDBK.NS": 0.350418155949619,
  "INFY.NS": -11.216354251562281,
  "ITC.NS": -7.249756429137889,
  "JSWSTEEL.NS": -2.469422028353337,
  "KOTAKBANK.NS": -3.185401246306407,
  "LT.NS": 5.985295922351745,
  "M&M.NS": -3.2584317032040473,
  "MARUTI.NS": 1.5180797686878051,
  "NESTLEIND.NS": -0.5531232948689518,
  "NTPC.NS": 1.2870265914584944,
  "ONGC.NS": -0.4843182219086328,
  "POWERGRID.NS": -0.6079399812441144,
  "RELIANCE.NS": -12.47014568823382,
  "SBILIFE.NS": -0.9686204036494288,
  "SBIN.NS": -2.75337098906383,
  "SUNPHARMA.NS": -1.5971373152297326,
  "TATACONSUM.NS": -2.4547430564873323,
  "TATAMOTORS.NS": -0.8281290590741522,
  "TATASTEEL.NS": -1.0304273504273407,
  "TCS.NS": -11.791213448227152,
  "TECHM.NS": -3.27285981308412,
  "TITAN.NS": -3.5840935096537003,
  "ULTRACEMCO.NS": 1.48820411975814,
  "WIPRO.NS": -1.74115500214686
}
rows =[{
      "Close": 1516.5,
      "High": 1519.9,
      "Low": 1486.0,
      "Name": "HDFC BANK",
      "Open": 1487.5,
      "change": 23.90000000000009,
      "id": 1,
      "percent": 1.601232748224581,
      "symbol": "HDFCBANK.NS",
      "volume": 15530103
    },
    {
      "Close": 1389.5,
      "High": 1397.75,
      "Low": 1374.05,
      "Name": "BHARTI AIRTEL LTD",
      "Open": 1375.5,
      "change": 15.450000000000045,
      "id": 15,
      "percent": 1.1244132309595753,
      "symbol": "BHARTIARTL.NS",
      "volume": 5622368
    },
    {
      "Close": 654.7,
      "High": 663.35,
      "Low": 641.6,
      "Name": "BHARAT PETROL CORP",
      "Open": 647.0,
      "change": 7.25,
      "id": 14,
      "percent": 1.1197775890030117,
      "symbol": "BPCL.NS",
      "volume": 8104262
    },
    {
      "Close": 3621.0,
      "High": 3659.0,
      "Low": 3582.3,
      "Name": "LARSEN & TOUBRO",
      "Open": 3586.0,
      "change": 35.59999999999991,
      "id": 32,
      "percent": 0.9929157137278939,
      "symbol": "LT.NS",
      "volume": 2740360
    },
    {
      "Close": 10237.95,
      "High": 10369.0,
      "Low": 10122.55,
      "Name": "ULTRATECH CEMENT",
      "Open": 10165.0,
      "change": 67.45000000000073,
      "id": 49,
      "percent": 0.663192566737139,
      "symbol": "ULTRACEMCO.NS",
      "volume": 519418
    },
    {
      "Close": 1172.95,
      "High": 1177.0,
      "Low": 1160.6,
      "Name": "AXIS BANK",
      "Open": 1165.5,
      "change": 7.7000000000000455,
      "id": 3,
      "percent": 0.6608024029178327,
      "symbol": "AXISBANK.NS",
      "volume": 8814997
    },
    {
      "Close": 374.5,
      "High": 378.15,
      "Low": 368.7,
      "Name": "NTPC LTD",
      "Open": 373.0,
      "change": 2.1999999999999886,
      "id": 35,
      "percent": 0.5909213000268569,
      "symbol": "NTPC.NS",
      "volume": 13317821
    },
    {
      "Close": 500.15,
      "High": 505.4,
      "Low": 489.15,
      "Name": "COAL INDIA LTD",
      "Open": 495.95,
      "change": 2.849999999999966,
      "id": 18,
      "percent": 0.5730947114417788,
      "symbol": "COALINDIA.NS",
      "volume": 12190536
    },
    {
      "Close": 4880.15,
      "High": 4908.0,
      "Low": 4807.4,
      "Name": "EICHER MOTORS",
      "Open": 4822.5,
      "change": 27.299999999999272,
      "id": 21,
      "percent": 0.5625560237798257,
      "symbol": "EICHERMOT.NS",
      "volume": 545727
    },
    {
      "Close": 13000.05,
      "High": 13034.0,
      "Low": 12811.0,
      "Name": "MARUTI SUZUKI IND",
      "Open": 12865.0,
      "change": 65.14999999999964,
      "id": 34,
      "percent": 0.5036761010908444,
      "symbol": "MARUTI.NS",
      "volume": 624801
    },
    {
      "Close": 678.8,
      "High": 690.45,
      "Low": 671.05,
      "Name": "HINDALCO INDS",
      "Open": 679.25,
      "change": 2.0,
      "id": 26,
      "percent": 0.2955082742316785,
      "symbol": "HINDALCO.NS",
      "volume": 15930052
    },
    {
      "Close": 4844.0,
      "High": 4860.0,
      "Low": 4821.5,
      "Name": "LTIMINDTREE LIMITED",
      "Open": 4843.0,
      "change": 12.699999999999818,
      "id": 31,
      "percent": 0.26286920704571887,
      "symbol": "LTIM.NS",
      "volume": 233454
    },
    {
      "Close": 1443.55,
      "High": 1448.75,
      "Low": 1427.85,
      "Name": "INDUSIND BANK LTD",
      "Open": 1441.0,
      "change": 2.7000000000000455,
      "id": 6,
      "percent": 0.1873893882083524,
      "symbol": "INDUSINDBK.NS",
      "volume": 2155290
    },
    {
      "Close": 2404.0,
      "High": 2428.95,
      "Low": 2362.7,
      "Name": "SHRIRAM FINANCE LIMITED",
      "Open": 2399.85,
      "change": 3.550000000000182,
      "id": 41,
      "percent": 0.1478889374908947,
      "symbol": "SHRIRAMFIN.NS",
      "volume": 975465
    },
    {
      "Close": 4116.0,
      "High": 4175.0,
      "Low": 4105.55,
      "Name": "DIVI'S LABORATORIE",
      "Open": 4113.0,
      "change": 3.0,
      "id": 19,
      "percent": 0.07293946024799416,
      "symbol": "DIVISLAB.NS",
      "volume": 612183
    },
    {
      "Close": 8966.4,
      "High": 9024.0,
      "Low": 8870.1,
      "Name": "BAJAJ AUTO LTD",
      "Open": 8980.0,
      "change": 2.9499999999989086,
      "id": 11,
      "percent": 0.03291143477119757,
      "symbol": "BAJAJ-AUTO.NS",
      "volume": 455920
    },
    {
      "Close": 6828.8,
      "High": 6910.0,
      "Low": 6793.0,
      "Name": "BAJAJ FINANCE LTD",
      "Open": 6820.0,
      "change": 2.1500000000005457,
      "id": 12,
      "percent": 0.031494217515187474,
      "symbol": "BAJFINANCE.NS",
      "volume": 742043
    },
    {
      "Close": 5970.0,
      "High": 5971.85,
      "Low": 5867.0,
      "Name": "APOLLO HOSPITALS.",
      "Open": 5938.3,
      "change": -0.0500000000001819,
      "id": 9,
      "percent": -0.0008375139236720278,
      "symbol": "APOLLOHOSP.NS",
      "volume": 608807
    },
    {
      "Close": 565.2,
      "High": 571.8,
      "Low": 563.45,
      "Name": "HDFC LIFE INSURANC",
      "Open": 565.0,
      "change": -0.4499999999999318,
      "id": 24,
      "percent": -0.07955449482894578,
      "symbol": "HDFCLIFE.NS",
      "volume": 3433290
    },
    {
      "Close": 1486.7,
      "High": 1493.9,
      "Low": 1479.05,
      "Name": "CIPLA LTD",
      "Open": 1489.15,
      "change": -2.4500000000000455,
      "id": 17,
      "percent": -0.1645233858241309,
      "symbol": "CIPLA.NS",
      "volume": 758326
    },
    {
      "Close": 1132.4,
      "High": 1135.0,
      "Low": 1124.15,
      "Name": "ICICI BANK",
      "Open": 1130.0,
      "change": -2.099999999999909,
      "id": 2,
      "percent": -0.18510356985455345,
      "symbol": "ICICIBANK.NS",
      "volume": 6312670
    },
    {
      "Close": 3381.0,
      "High": 3457.85,
      "Low": 3355.6,
      "Name": "ADANI ENTERPRISES",
      "Open": 3406.0,
      "change": -6.300000000000182,
      "id": 7,
      "percent": -0.1859888406695652,
      "symbol": "ADANIENT.NS",
      "volume": 3473668
    },
    {
      "Close": 1605.0,
      "High": 1620.0,
      "Low": 1597.05,
      "Name": "BAJAJ FINSERV LTD",
      "Open": 1609.0,
      "change": -3.4500000000000455,
      "id": 13,
      "percent": -0.21449221300009605,
      "symbol": "BAJAJFINSV.NS",
      "volume": 566278
    },
    {
      "Close": 319.05,
      "High": 322.95,
      "Low": 317.4,
      "Name": "POWER GRID CORP",
      "Open": 318.0,
      "change": -0.8499999999999659,
      "id": 38,
      "percent": -0.26570803376053953,
      "symbol": "POWERGRID.NS",
      "volume": 15058182
    },
    {
      "Close": 282.65,
      "High": 285.95,
      "Low": 281.85,
      "Name": "OIL & NATURAL GAS",
      "Open": 284.0,
      "change": -0.8000000000000114,
      "id": 37,
      "percent": -0.2822367260539818,
      "symbol": "ONGC.NS",
      "volume": 11041667
    },
    {
      "Close": 2467.0,
      "High": 2485.0,
      "Low": 2458.05,
      "Name": "NESTLE INDIA",
      "Open": 2476.95,
      "change": -7.150000000000091,
      "id": 36,
      "percent": -0.28898813734010026,
      "symbol": "NESTLEIND.NS",
      "volume": 453772
    },
    {
      "Close": 174.9,
      "High": 177.55,
      "Low": 174.15,
      "Name": "TATA STEEL LTD",
      "Open": 174.95,
      "change": -0.5999999999999943,
      "id": 46,
      "percent": -0.3418803418803386,
      "symbol": "TATASTEEL.NS",
      "volume": 38674485
    },
    {
      "Close": 958.9,
      "High": 970.95,
      "Low": 958.0,
      "Name": "TATA MOTORS LTD.",
      "Open": 962.5,
      "change": -3.4500000000000455,
      "id": 45,
      "percent": -0.3584974281706287,
      "symbol": "TATAMOTORS.NS",
      "volume": 9590588
    },
    {
      "Close": 1702.0,
      "High": 1717.85,
      "Low": 1694.7,
      "Name": "KOTAK MAHINDRA BAN",
      "Open": 1711.0,
      "change": -7.0499999999999545,
      "id": 5,
      "percent": -0.4125098739065536,
      "symbol": "KOTAKBANK.NS",
      "volume": 4936177
    },
    {
      "Close": 2443.65,
      "High": 2474.8,
      "Low": 2431.6,
      "Name": "GRASIM INDUSTRIES",
      "Open": 2449.75,
      "change": -10.150000000000091,
      "id": 22,
      "percent": -0.41364414377700265,
      "symbol": "GRASIM.NS",
      "volume": 483000
    },
    {
      "Close": 2959.0,
      "High": 2977.0,
      "Low": 2952.2,
      "Name": "RELIANCE INDS",
      "Open": 2967.25,
      "change": -13.099999999999909,
      "id": 39,
      "percent": -0.44076578849971093,
      "symbol": "RELIANCE.NS",
      "volume": 3547388
    },
    {
      "Close": 828.0,
      "High": 841.25,
      "Low": 827.0,
      "Name": "STATE BK OF INDIA",
      "Open": 830.0,
      "change": -4.100000000000023,
      "id": 4,
      "percent": -0.4927292392741285,
      "symbol": "SBIN.NS",
      "volume": 12252075
    },
    {
      "Close": 5867.0,
      "High": 5909.1,
      "Low": 5838.5,
      "Name": "DR REDDYS LABS",
      "Open": 5896.4,
      "change": -30.699999999999818,
      "id": 20,
      "percent": -0.5205419061668077,
      "symbol": "DRREDDY.NS",
      "volume": 424443
    },
    {
      "Close": 1487.0,
      "High": 1505.7,
      "Low": 1477.1,
      "Name": "SUN PHARMACEUTICAL",
      "Open": 1504.0,
      "change": -8.099999999999909,
      "id": 42,
      "percent": -0.5417697812855267,
      "symbol": "SUNPHARMA.NS",
      "volume": 5307322
    },
    {
      "Close": 5247.0,
      "High": 5285.15,
      "Low": 5219.0,
      "Name": "BRITANNIA INDS",
      "Open": 5260.1,
      "change": -34.149999999999636,
      "id": 16,
      "percent": -0.6466394629957422,
      "symbol": "BRITANNIA.NS",
      "volume": 268208
    },
    {
      "Close": 2366.75,
      "High": 2383.25,
      "Low": 2364.7,
      "Name": "HINDUSTAN UNILEVER",
      "Open": 2378.5,
      "change": -15.75,
      "id": 27,
      "percent": -0.6610703043022036,
      "symbol": "HINDUNILVR.NS",
      "volume": 974100
    },
    {
      "Close": 1462.6,
      "High": 1475.5,
      "Low": 1460.0,
      "Name": "INFOSYS LTD",
      "Open": 1468.25,
      "change": -9.800000000000182,
      "id": 29,
      "percent": -0.6655800054333184,
      "symbol": "INFY.NS",
      "volume": 5277938
    },
    {
      "Close": 1437.0,
      "High": 1448.45,
      "Low": 1433.45,
      "Name": "SBI LIFE INSURANCE",
      "Open": 1442.5,
      "change": -9.799999999999955,
      "id": 40,
      "percent": -0.6773569256289712,
      "symbol": "SBILIFE.NS",
      "volume": 487961
    },
    {
      "Close": 5105.0,
      "High": 5198.15,
      "Low": 5080.05,
      "Name": "HERO MOTOCORP LTD",
      "Open": 5105.1,
      "change": -40.19999999999982,
      "id": 25,
      "percent": -0.7813107362201628,
      "symbol": "HEROMOTOCO.NS",
      "volume": 458258
    },
    {
      "Close": 462.15,
      "High": 470.5,
      "Low": 462.0,
      "Name": "WIPRO LTD",
      "Open": 467.0,
      "change": -3.650000000000034,
      "id": 50,
      "percent": -0.7835981107771648,
      "symbol": "WIPRO.NS",
      "volume": 4102763
    },
    {
      "Close": 1342.5,
      "High": 1360.0,
      "Low": 1340.85,
      "Name": "HCL TECHNOLOGIES",
      "Open": 1360.0,
      "change": -11.049999999999955,
      "id": 23,
      "percent": -0.8163717631413656,
      "symbol": "HCLTECH.NS",
      "volume": 1769966
    },
    {
      "Close": 436.55,
      "High": 442.45,
      "Low": 435.3,
      "Name": "ITC LTD",
      "Open": 441.0,
      "change": -4.800000000000011,
      "id": 28,
      "percent": -1.0875722215928427,
      "symbol": "ITC.NS",
      "volume": 12761457
    },
    {
      "Close": 3850.95,
      "High": 3883.8,
      "Low": 3844.3,
      "Name": "TATA CONSULTANCY S",
      "Open": 3878.25,
      "change": -42.5,
      "id": 43,
      "percent": -1.0915768791174922,
      "symbol": "TCS.NS",
      "volume": 1309452
    },
    {
      "Close": 2870.0,
      "High": 2910.2,
      "Low": 2867.0,
      "Name": "ASIAN PAINTS LTD",
      "Open": 2910.2,
      "change": -33.75,
      "id": 10,
      "percent": -1.162290142057684,
      "symbol": "ASIANPAINT.NS",
      "volume": 755822
    },
    {
      "Close": 3411.0,
      "High": 3455.05,
      "Low": 3404.2,
      "Name": "TITAN COMPANY LTD",
      "Open": 3452.1,
      "change": -41.05000000000018,
      "id": 48,
      "percent": -1.1891484769919376,
      "symbol": "TITAN.NS",
      "volume": 878625
    },
    {
      "Close": 906.05,
      "High": 925.0,
      "Low": 906.05,
      "Name": "JSW STEEL LTD",
      "Open": 915.0,
      "change": -10.950000000000045,
      "id": 30,
      "percent": -1.1941112322791763,
      "symbol": "JSWSTEEL.NS",
      "volume": 2113036
    },
    {
      "Close": 2576.45,
      "High": 2605.0,
      "Low": 2572.4,
      "Name": "MAHINDRA &MAHINDRA",
      "Open": 2589.8,
      "change": -32.75,
      "id": 33,
      "percent": -1.2551739996933926,
      "symbol": "M&M.NS",
      "volume": 2919241
    },
    {
      "Close": 1318.55,
      "High": 1345.0,
      "Low": 1318.0,
      "Name": "TECH MAHINDRA",
      "Open": 1337.5,
      "change": -18.950000000000045,
      "id": 47,
      "percent": -1.4168224299065455,
      "symbol": "TECHM.NS",
      "volume": 1288301
    },
    {
      "Close": 1099.05,
      "High": 1111.0,
      "Low": 1096.0,
      "Name": "TATA CONSUMER PRODUCT LTD",
      "Open": 1111.0,
      "change": -18.90000000000009,
      "id": 44,
      "percent": -1.690594391520201,
      "symbol": "TATACONSUM.NS",
      "volume": 1424791
    },
    {
      "Close": 1416.9,
      "High": 1444.95,
      "Low": 1382.15,
      "Name": "ADANI PORT SPECIAL",
      "Open": 1435.0,
      "change": -26.449999999999818,
      "id": 8,
      "percent": -1.8325423493954909,
      "symbol": "ADANIPORTS.NS",
      "volume": 19100263
    }
  ]
total_data={"index_data": [{"Name": "NIFTY50", "Symbol": "^NSEI", "Close": 22604.849609375, "High": 22783.349609375, "Low": 22568.400390625, "change": -38.55078125, "percent": -0.170251731563962}, {"Name": "SENSEX", "Symbol": "^BSESN", "Close": 74482.78125, "High": 75111.390625, "Low": 74346.3984375, "change": -188.5, "percent": -0.25243975574612226}, {"Name": "BANK-NIFTY", "Symbol": "^NSEBANK", "Close": 49396.75, "High": 49974.75, "Low": 49249.8984375, "change": -27.30078125, "percent": -0.05523784638946894}], "chart_table": [{"Name": "NIFTY50", "Symbol": "^NSEI", "Close": 22604.849609375, "High": 22783.349609375, "Low": 22568.400390625, "change": -38.55078125, "percent": -0.170251731563962}, {"Name": "SENSEX", "Symbol": "^BSESN", "Close": 74482.78125, "High": 75111.390625, "Low": 74346.3984375, "change": -188.5, "percent": -0.25243975574612226}, {"Name": "BANK-NIFTY", "Symbol": "^NSEBANK", "Close": 49396.75, "High": 49974.75, "Low": 49249.8984375, "change": -27.30078125, "percent": -0.05523784638946894}, {"Name": "NIFTY-IT", "Symbol": "^CNXIT", "Close": 33200.94921875, "High": 33688.94921875, "Low": 33145.8984375, "change": -378.44921875, "percent": -1.1270279884685621}, {"Name": "NIFTY-FINANCE", "Symbol": "NIFTY_FIN_SERVICE.NS", "Close": 21841.150390625, "High": 22073.69921875, "Low": 21779.19921875, "change": 29.951171875, "percent": 0.13732015179271972}, {"Name": "NIFTY-ENERGY", "Symbol": "^CNXENERGY", "Close": 40366.69921875, "High": 40771.3515625, "Low": 40311.3515625, "change": 14.59765625, "percent": 0.036175702589839556}], "chart_data": {"time": ["09:15", "09:30", "09:45", "10:00", "10:15", "10:30", "10:45", "11:00", "11:15", "11:30", "11:45", "12:00", "12:15", "12:30", "12:45", "13:00", "13:15", "13:30", "13:45", "14:00", "14:15", "14:30", "14:45", "15:00", "15:15"], "NIFTY50": [22679, 22706, 22746, 22727, 22733, 22743, 22745, 22734, 22729, 22735, 22745, 22745, 22747, 22742, 22738, 22715, 22733, 22740, 22739, 22768, 22773, 22744, 22694, 22604, 22588], "SENSEX": [74747, 74833, 74982, 74919, 74966, 74980, 74982, 74959, 74938, 74962, 74980, 74986, 74978, 74959, 74950, 74865, 74916, 74939, 74918, 75065, 75079, 74982, 74806, 74479, 74483], "BANK-NIFTY": [49402, 49396, 49639, 49504, 49563, 49558, 49601, 49588, 49543, 49576, 49570, 49563, 49530, 49525, 49515, 49463, 49483, 49518, 49576, 49913, 49936, 49818, 49617, 49410, 49291], "NIFTY-IT": [33550, 33657, 33602, 33552, 33528, 33511, 33475, 33444, 33446, 33447, 33464, 33486, 33505, 33471, 33465, 33441, 33467, 33455, 33448, 33429, 33432, 33401, 33362, 33187, 33212], "NIFTY-FINANCE": [21811, 21819, 21915, 21878, 21901, 21908, 21950, 21935, 21916, 21931, 21943, 21950, 21942, 21938, 21915, 21888, 21892, 21915, 21926, 22021, 22058, 22026, 21946, 21834, 21802], "NIFTY-ENERGY": [40487, 40537, 40649, 40621, 40562, 40565, 40545, 40586, 40585, 40650, 40693, 40689, 40708, 40757, 40724, 40633, 40709, 40720, 40753, 40699, 40706, 40501, 40479, 40383, 40355]}, "top_gainers": [{"Name": "Mahindra", "Symbol": "M&M.NS", "Close": 2156.35009765625, "High": 2169.0, "Low": 2073.050048828125, "change": 94.300048828125, "percent": 4.573121243187878}, {"Name": "Power Grid", "Symbol": "POWERGRID.NS", "Close": 301.8500061035156, "High": 304.3500061035156, "Low": 293.04998779296875, "change": 8.149993896484375, "percent": 2.7749382219090224}, {"Name": "Shriram Finance", "Symbol": "SHRIRAMFIN.NS", "Close": 2551.699951171875, "High": 2578.800048828125, "Low": 2484.0, "change": 59.5, "percent": 2.3874488871577935}, {"Name": "Hero MotoCorp", "Symbol": "HEROMOTOCO.NS", "Close": 4543.0498046875, "High": 4588.2001953125, "Low": 4465.0, "change": 85.349609375, "percent": 1.9146556662727001}, {"Name": "IndusInd Bank", "Symbol": "INDUSINDBK.NS", "Close": 1515.699951171875, "High": 1537.0, "Low": 1489.0, "change": 28.449951171875, "percent": 1.9129232591612038}, {"Name": "Bajaj Auto", "Symbol": "BAJAJ-AUTO.NS", "Close": 8903.650390625, "High": 8966.0, "Low": 8795.0, "change": 143.55078125, "percent": 1.6386889150937611}], "top_losers": [{"Name": "Tech Mahindra", "Symbol": "TECHM.NS", "Close": 1263.5, "High": 1291.0999755859375, "Low": 1260.050048828125, "change": -24.800048828125, "percent": -1.9250211820362688}, {"Name": "Bharat Petroleum", "Symbol": "BPCL.NS", "Close": 607.3499755859375, "High": 624.5499877929688, "Low": 603.4000244140625, "change": -11.45001220703125, "percent": -1.8503575360221352}, {"Name": "JSW Steel", "Symbol": "JSWSTEEL.NS", "Close": 882.2000122070312, "High": 902.75, "Low": 880.0499877929688, "change": -13.54998779296875, "percent": -1.5126974929353894}, {"Name": "HCL Technologies", "Symbol": "HCLTECH.NS", "Close": 1366.5999755859375, "High": 1397.9000244140625, "Low": 1362.449951171875, "change": -20.800048828125, "percent": -1.4992106430810708}, {"Name": "Dr. Reddy's Laboratories", "Symbol": "DRREDDY.NS", "Close": 6204.2998046875, "High": 6313.0, "Low": 6185.0, "change": -92.80029296875, "percent": -1.4736988697907123}, {"Name": "Tata Steel", "Symbol": "TATASTEEL.NS", "Close": 165.0, "High": 168.39999389648438, "Low": 164.5, "change": -2.399993896484375, "percent": -1.4336881624789461}], "bar": {"percent": [1.8, 0.13, 0.03, -0.05, -0.16, -0.17, -0.25, -1.01, -1.13], "name": ["NIFTYAUTO", "NIFTY-FINANCE", "NIFTY-ENERGY", "BANK-NIFTY", "NIFTY-FMCG", "NIFTY50", "SENSEX", "NIFTY-METAL", "NIFTY-IT"]}, "heat_map": [{"Name": "Mahindra", "Symbol": "M&M.NS", "Close": 2156.35009765625, "High": 2169.0, "Low": 2073.050048828125, "change": 94.300048828125, "percent": 4.573121243187878}, {"Name": "Power Grid", "Symbol": "POWERGRID.NS", "Close": 301.8500061035156, "High": 304.3500061035156, "Low": 293.04998779296875, "change": 8.149993896484375, "percent": 2.7749382219090224}, {"Name": "Shriram Finance", "Symbol": "SHRIRAMFIN.NS", "Close": 2551.699951171875, "High": 2578.800048828125, "Low": 2484.0, "change": 59.5, "percent": 2.3874488871577935}, {"Name": "Hero MotoCorp", "Symbol": "HEROMOTOCO.NS", "Close": 4543.0498046875, "High": 4588.2001953125, "Low": 4465.0, "change": 85.349609375, "percent": 1.9146556662727001}, {"Name": "IndusInd Bank", "Symbol": "INDUSINDBK.NS", "Close": 1515.699951171875, "High": 1537.0, "Low": 1489.0, "change": 28.449951171875, "percent": 1.9129232591612038}, {"Name": "Bajaj Auto", "Symbol": "BAJAJ-AUTO.NS", "Close": 8903.650390625, "High": 8966.0, "Low": 8795.0, "change": 143.55078125, "percent": 1.6386889150937611}, {"Name": "HDFC Life Insurance Company", "Symbol": "HDFCLIFE.NS", "Close": 583.6500244140625, "High": 588.5, "Low": 576.0499877929688, "change": 8.550048828125, "percent": 1.4867065190558961}, {"Name": "Bajaj Finance", "Symbol": "BAJFINANCE.NS", "Close": 6923.5498046875, "High": 6975.0, "Low": 6821.9501953125, "change": 96.94970703125, "percent": 1.4201755726768786}, {"Name": "Bajaj Finserv", "Symbol": "BAJAJFINSV.NS", "Close": 1615.0, "High": 1633.949951171875, "Low": 1591.300048828125, "change": 19.3499755859375, "percent": 1.2126704032761189}, {"Name": "Grasim Industries", "Symbol": "GRASIM.NS", "Close": 2411.64990234375, "High": 2438.449951171875, "Low": 2374.10009765625, "change": 25.0498046875, "percent": 1.04960209764929}, {"Name": "Maruti Suzuki", "Symbol": "MARUTI.NS", "Close": 12817.5, "High": 12996.0, "Low": 12740.2001953125, "change": 127.650390625, "percent": 1.0059251650287055}, {"Name": "SBI LIC", "Symbol": "SBILIFE.NS", "Close": 1436.550048828125, "High": 1449.8499755859375, "Low": 1423.199951171875, "change": 14.2000732421875, "percent": 0.9983529712044165}, {"Name": "Tata Consumer Products", "Symbol": "TATACONSUM.NS", "Close": 1108.3499755859375, "High": 1114.25, "Low": 1095.6500244140625, "change": 9.8499755859375, "percent": 0.896675064718935}, {"Name": "Tata Motors", "Symbol": "TATAMOTORS.NS", "Close": 1007.9000244140625, "High": 1019.4500122070312, "Low": 997.5, "change": 7.300048828125, "percent": 0.7295671603280015}, {"Name": "Adani Ports", "Symbol": "ADANIPORTS.NS", "Close": 1324.9000244140625, "High": 1334.6500244140625, "Low": 1316.25, "change": 7.6500244140625, "percent": 0.5807572149601443}, {"Name": "Axis Bank", "Symbol": "AXISBANK.NS", "Close": 1165.9000244140625, "High": 1182.9000244140625, "Low": 1155.1500244140625, "change": 6.6500244140625, "percent": 0.5736488603892603}, {"Name": "Eicher Motors", "Symbol": "EICHERMOT.NS", "Close": 4597.39990234375, "High": 4689.9501953125, "Low": 4578.0, "change": 25.5498046875, "percent": 0.5588504465751853}, {"Name": "Divi's Laboratories", "Symbol": "DIVISLAB.NS", "Close": 4002.39990234375, "High": 4066.0, "Low": 3973.60009765625, "change": 13.14990234375, "percent": 0.3296334484865576}, {"Name": "Asian Paints", "Symbol": "ASIANPAINT.NS", "Close": 2875.89990234375, "High": 2912.0, "Low": 2855.0, "change": 7.699951171875, "percent": 0.26845935788852493}, {"Name": "Coal India", "Symbol": "COALINDIA.NS", "Close": 454.29998779296875, "High": 458.3999938964844, "Low": 452.04998779296875, "change": 1.04998779296875, "percent": 0.23165753843767237}, {"Name": "Hindustan Unilever", "Symbol": "HINDUNILVR.NS", "Close": 2230.449951171875, "High": 2240.25, "Low": 2225.0, "change": 4.349853515625, "percent": 0.19540242238903563}, {"Name": "Reliance Industries", "Symbol": "RELIANCE.NS", "Close": 2934.0, "High": 2966.14990234375, "Low": 2925.75, "change": 3.949951171875, "percent": 0.134808317470713}, {"Name": "UltraTech Cement", "Symbol": "ULTRACEMCO.NS", "Close": 9971.849609375, "High": 10180.0, "Low": 9911.349609375, "change": 7.3994140625, "percent": 0.07425812681547497}, {"Name": "NTPC", "Symbol": "NTPC.NS", "Close": 363.20001220703125, "High": 365.45001220703125, "Low": 359.29998779296875, "change": 0.20001220703125, "percent": 0.055099781551308534}, {"Name": "State Bank of India", "Symbol": "SBIN.NS", "Close": 826.25, "High": 834.8499755859375, "Low": 819.9000244140625, "change": -0.25, "percent": -0.030248033877797946}, {"Name": "Nestle India", "Symbol": "NESTLEIND.NS", "Close": 2507.39990234375, "High": 2537.60009765625, "Low": 2500.550048828125, "change": -2.400146484375, "percent": -0.09563098404973239}, {"Name": "Wipro", "Symbol": "WIPRO.NS", "Close": 462.3999938964844, "High": 466.75, "Low": 461.5, "change": -0.550018310546875, "percent": -0.1188072785493106}, {"Name": "Oil & Natural Gas", "Symbol": "ONGC.NS", "Close": 282.8500061035156, "High": 286.3500061035156, "Low": 281.45001220703125, "change": -0.350006103515625, "percent": -0.1235897204904623}, {"Name": "Apollo Hospitals", "Symbol": "APOLLOHOSP.NS", "Close": 5947.10009765625, "High": 6023.0, "Low": 5901.0, "change": -21.25, "percent": -0.3560447971767742}, {"Name": "Titan Company", "Symbol": "TITAN.NS", "Close": 3589.25, "High": 3619.5, "Low": 3580.0, "change": -15.60009765625, "percent": -0.4327530197827823}, {"Name": "Britannia Industries", "Symbol": "BRITANNIA.NS", "Close": 4775.9501953125, "High": 4825.0, "Low": 4765.10009765625, "change": -23.89990234375, "percent": -0.49793018234924125}, {"Name": "Cipla", "Symbol": "CIPLA.NS", "Close": 1400.0, "High": 1418.949951171875, "Low": 1395.050048828125, "change": -8.0, "percent": -0.5681818181818182}, {"Name": "ITC", "Symbol": "ITC.NS", "Close": 435.6499938964844, "High": 440.5, "Low": 435.1000061035156, "change": -2.550018310546875, "percent": -0.5819302235304589}, {"Name": "HDFC Bank", "Symbol": "HDFCBANK.NS", "Close": 1520.0999755859375, "High": 1539.5, "Low": 1514.9000244140625, "change": -9.4000244140625, "percent": -0.6145815242930697}, {"Name": "Bharti Airtel", "Symbol": "BHARTIARTL.NS", "Close": 1322.300048828125, "High": 1334.800048828125, "Low": 1319.949951171875, "change": -10.14990234375, "percent": -0.7617473613041356}, {"Name": "LTIMindtree", "Symbol": "LTIM.NS", "Close": 4706.39990234375, "High": 4778.60009765625, "Low": 4699.9501953125, "change": -37.55029296875, "percent": -0.7915406238002555}, {"Name": "ICICI Bank", "Symbol": "ICICIBANK.NS", "Close": 1150.4000244140625, "High": 1169.550048828125, "Low": 1146.75, "change": -9.75, "percent": -0.8404085501721442}, {"Name": "Adani Enterprises", "Symbol": "ADANIENT.NS", "Close": 3054.699951171875, "High": 3108.449951171875, "Low": 3045.0, "change": -26.5, "percent": -0.8600545378407277}, {"Name": "Hindalco Industries", "Symbol": "HINDALCO.NS", "Close": 644.4000244140625, "High": 653.7000122070312, "Low": 642.2999877929688, "change": -5.64996337890625, "percent": -0.8691582932089338}, {"Name": "Infosys", "Symbol": "INFY.NS", "Close": 1420.550048828125, "High": 1436.550048828125, "Low": 1417.550048828125, "change": -14.199951171875, "percent": -0.9897160600714411}, {"Name": "Kotak Mahindra Bank", "Symbol": "KOTAKBANK.NS", "Close": 1623.949951171875, "High": 1647.0, "Low": 1620.0, "change": -16.4500732421875, "percent": -1.0028086440722488}, {"Name": "Larsen & Toubro", "Symbol": "LT.NS", "Close": 3594.300048828125, "High": 3648.949951171875, "Low": 3584.050048828125, "change": -40.0, "percent": -1.1006245896757463}, {"Name": "Tata Consultancy Services", "Symbol": "TCS.NS", "Close": 3820.64990234375, "High": 3881.75, "Low": 3810.0, "change": -49.550048828125, "percent": -1.2802968697553085}, {"Name": "Sun Pharmaceutical", "Symbol": "SUNPHARMA.NS", "Close": 1502.0999755859375, "High": 1529.1500244140625, "Low": 1497.0, "change": -19.5, "percent": -1.281545761887315}, {"Name": "Tata Steel", "Symbol": "TATASTEEL.NS", "Close": 165.0, "High": 168.39999389648438, "Low": 164.5, "change": -2.399993896484375, "percent": -1.4336881624789461}, {"Name": "Dr. Reddy's Laboratories", "Symbol": "DRREDDY.NS", "Close": 6204.2998046875, "High": 6313.0, "Low": 6185.0, "change": -92.80029296875, "percent": -1.4736988697907123}, {"Name": "HCL Technologies", "Symbol": "HCLTECH.NS", "Close": 1366.5999755859375, "High": 1397.9000244140625, "Low": 1362.449951171875, "change": -20.800048828125, "percent": -1.4992106430810708}, {"Name": "JSW Steel", "Symbol": "JSWSTEEL.NS", "Close": 882.2000122070312, "High": 902.75, "Low": 880.0499877929688, "change": -13.54998779296875, "percent": -1.5126974929353894}, {"Name": "Bharat Petroleum", "Symbol": "BPCL.NS", "Close": 607.3499755859375, "High": 624.5499877929688, "Low": 603.4000244140625, "change": -11.45001220703125, "percent": -1.8503575360221352}, {"Name": "Tech Mahindra", "Symbol": "TECHM.NS", "Close": 1263.5, "High": 1291.0999755859375, "Low": 1260.050048828125, "change": -24.800048828125, "percent": -1.9250211820362688}]}
