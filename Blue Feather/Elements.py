class ElementsInfo:
    elementsInfoList = [
        "Bir ametaldir. Standart sıcaklık ve basınç altında renksiz, kokusuz, metalik olmayan, tatsız, oldukça yanıcı ve H2 olarak bulunan bir diatomik gazdır.\n Tüm elementler arasında en hafif elementtir. Evrenin kütlesinin %75'ini oluşturan ve evrende en çok bulunan elementtir.\nElement serisi : Ametaller\nMaddenin hâli : Gaz",                                                                                                                                     
        "En hafif 2. gazdır. Renksiz, kokusuz yanıcı olmayan bir gaz elementtir.\n Asal gazlar grubundan olduğu için tepkimeye girmez ve bu yüzden eylemsizdir.\nElement serisi : Soygazlar\nMaddenin hâli : Gaz",
        "Yoğunluğu en düşük olan metaldir. Doğada saf halde bulunmaz. Yumuşak ve gümüşümsü beyaz metaldir.\n Bu metal doldurulabilir pillerde (örnek olarak cep telefonu ve kamera pili) ve ağırla yüksek direniş göstermesi sebebiyle alaşım olarak hava taşıtlarında kullanılır.\nElement serisi : Alkali metaller \nMaddenin hâli : Katı",
        "Ender elementlerdendir. Yerkabuğunda ancak %0,0006 oranında bulunur. Zengin yatakları bulunmadığından, berilden elde edilir.\nAlüminyumdan daha hafif, ama daha sert, erime noktası da yüksek bir element\nElement serisi : Alkalinler\nMaddenin hâli : Katı",
        "Metal ile ametal arası yarı iletken özelliği bulunan bir elementtir. \nAna kullanım alanları, çamaşır tozunda beyazlatıcı olarak, cam, seramiklerde ve tarımda kullanılır. Ayrıca Türkiye, dünya rezervlerinin yüzde 73’üne sahip.\nElement serisi : Yarı metaller\nMaddenin hâli : Katı",
        "Dünyadaki tüm yaşamın temelini oluşturur. Evrende bolluk bakımından altıncı sırada yer alır. Dünyada hem doğal halde, hem de başka elementlerle bileşik halinde bulunur.\nEn çok kömür yataklarından elde edilir. Amorf, grafit ve elmas olmak üzere doğal olarak meydana gelen üç allotropu vardır.\nElement serisi : Ametaller \nMaddenin hâli : Katı",
        "Nitrojen olarakta bilinir. Dünya atmosferinin %78'ini oluşturur ve tüm canlı dokularında bulunur.\nRenksiz, kokusuz, tatsız gazdır. Gaz ve Sıvı halde bulunur.\nElement serisi : Ametaller\nMaddenin hâli : Gaz",
        "Gaz durumunda olan ve havada beşte bir oranında bulunan, hidrojenle birleşerek suyu oluşturan ve kimyasal olarak çok aktif olan bir elementtir.\nFotosentez sırasında bitkiler tarafından üretilen havanın önemli bir bileşenidir ve insanların ve hayvanların solunumu için gereklidir.\nElement serisi : Ametaller\nMaddenin  hâli : Gaz",
        "İnsan ve hayvanların kemik ve diş yapıları için gerekli ve önemli bir maddedir. Diş macunlarında da kullanılan ve dişlere beyazlık kazandıran maddedir.\nEn reaktif element olup O2 ve asal gazlar hariç tüm elementlerle hemen reaksiyona girer.\nElement serisi : Halojenler\nMaddenin hâli : Gaz",
        "Genellikle aydınlatma amacıyla kullanılan kimyasal bir elementtir. Reklam tabela ve panolarında kullanılan ışıklandırmaların kaynağı.\nEvrende bulunan en bol 4. Elementtir. Hiçbir madde ile reaksiyona girmez, bileşik oluşturmaz\nElement serisi : Soygazlar\nMaddenin hâli : Gaz",
        "Reaktif elementtir, doğada serbest olarak bulunmaz. Havada parlak beyaz alevle yanar. Ayrıca su ile temas ettiğinde de tutuşabileceğinden nemsiz ortamda saklanması gerekir.\nYer kabuğunun en bol altıncı elementidir. Sıvı hali nükleer santrallerde soğutucu olarak kullanılır, bir bileşiği olan (NaCı) yani yemek tuzudur.\nElement serisi : Alkali metaller \nMaddenin hâli : Katı",
        "Vücutta %60 oranında kemik ve dişlerde yer alır. Günlük ihtiyaç 0,2-0,3g kadar. Elektrikli fotoğraf makinesi flaşı çıkmadan önce, bu element yakılarak flaşlı fotoğraf çekilirdi.\nGümüş beyazlığında bir metaldir ve genellikle alaşım maddesi olarak, yani başka metallerle karıştırılarak kullanılır.\nElement serisi : Alkalinler\nMaddenin hâli : Katı",
        "Gümüşümsü beyaz renkte, sünek, hafif ve kolay işlenebilen metalik bir elementtir. Oksidasyona karşı üstün direnci ile tanınır..Yer kabuğunun en bol üçüncü elementi\nUçak ve roket parçalarından otomobil jantlarına, elektronik cihazlardan yapı malzemelerine, mutfak eşyalarından folyo ve meşrubat kutularına kadar birçok sektörde kullanılır.\nElement serisi : Metaller\nMaddenin hâli : Katı",
        "Silikon olarak da bilinir.Yarı iletkendir. Yeryüzü kabuğunun %27,7’lik kısmını oluşturmaktadır.Oksijenden sonra yer kabuğunda bulunan ikinci elementtir.\nbilgisayar yongaları, transistörler, diyotlar, sıvı kristal ekranlar ve diğer çeşitli elektronik ve anahtarlama cihazlarında kullanılan temel malzemedir\nElement serisi : Yarı metaller\nMaddenin hâli : Katı",
        "İnsan vücudunda kalsiyumdan sonra en fazla bulunan kimyasal elementtir.Bütün organizmalar için birleşimleri (fosfodiester bağları) DNA yapıları için büyük önem taşır.\nİnsan vücudu kemik ve diş oluşumu, hücre büyümesi ve onarımı, enerji üretimi, kalp kasının kasılması, sinir ve kas hareketleri, böbrek işlevleri açısından ihtiyaç duyar.\nElement serisi : Ametaller\nMaddenin hâli : katı",
        "Rengi kanarya sarısı,bal sarısı veya yeşilimsi sarı olabilir. 119°C'de eridiği için en kolay tanıma usulü kibrit alevine tutmaktır.\nAlevde katran gibi eriyerek siyah damlacıklar halinde damlamaya başlar. Hafif açık mavi renkli alevi vardır ve çıkan SO2 gazı zehirlidir.\nElement serisi : Ametaller\nMaddenin hâli : Katı",
        "Hafif antiseptik olması özelliğiyle, suyun dezenfeksiyon işlemi için suya katılır. Saf olarak çok tehlikeli bir maddedir.\nSıvı hali ciltte yanıklara, gaz hali mukus zarlarında tahrişe neden olur. Bu yüzden insanların etkileşimde bulunduğu sulara eser miktarlarda eklenir\nElement serisi : Halojenler\nMaddenin hâli : Gaz",
        "Sıvılaştırılmış atmosferik havanın fraksiyonel damıtılmasından elde edilir. Havadan oksijen ve nitrojen üretiminin bir yan ürünü olarak da elde edilir.\nAydınlatma ürünlerinde kullanılır ve beyazımsı açık mavi bir ışık verir. Genellikle akkor ampullerin doldurulmasında veya flüoresan lambalarda kripton ile karıştırılır.\nElement serisi : Soygazlar\nMaddenin hâli : Gaz",
        "Bıçakla kesilebilecek kadar yumuşaktır., soğukta sert ve kırılgan olan gümüşümsü-beyaz renkte metalik bir elementtir.\n hidroksit, sabun, deterjan ve gider temizleyici yapmak için kullanılır. Canlılarda sinir ve kas dokularının işlev görmesi için yaşamsal önemi olan bir elementtir\nElement serisi : Alkali metaller\nMaddenin hâli : katı",
        "Yeryüzünde en bol bulunan beşinci elementtir. Reaktivitesi yüksek olduğundan serbest halde bulunmaz. İnsan vücûdunda %99’u kemiklerde ve dişte bulunur.\nTebeşir, kireç taşı, mermer gibi minerallerden elde edilir. saf olarak sanayide önemli bir kullanım alanı yoktur.\nElement serisi : Alkalinler\nMaddenin hâli : Katı",
        "Oldukça yumuşak, gümüşümsü beyaz renkli bir metaldir. Yer kabuğunda en bol bulunan sekizinci (nadir toprak elementidir)\n1879 yılında İsveçli bilim adamı Lars Fredrik Nilson tarafından bulunmuştur.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Güçlü, hafif ve asitlere dayanıklı bir metaldir. Çelik kadar güçlü ve hafiftir. Eklem ve protezlerde, kemikleri sabitlemek için, diş implantlarında ve diğer biyolojik implantlarda kullanılır.\n Dayanıklılık, düşük ağırlık ve yüksek sıcaklıklara direncin önemli olduğu uçaklar, uzay araçları, füzeler ve roketlerde kullanılır. Ancak yüksek maliyeti yaygın kullanımını sınırlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Otomobil endüstrisi, uzay araçları ve uçak sanayinde titanyumlu alaşımlarla birlikte kullanılmaktadır. Sülfürik asit üretiminde katalizör olarak kullanılır\nnem, hava ve çoğu asit ve alkali ile korozyona dayanıklıdır. Bu yönüyle kimya endüstrisi için borular ve tüpler yapmak için kullanılır. 65 farklı mineralde bileşik halinde bulunur.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Çok sert olması ve erime noktasının 1857 °C olması nedeniyle  metallere sertlik sağlanması ve zırhlı araç yapımı için kullanılır.\nEn önemli kullanım alanı Nikel ile beraber paslanmaz çeliklerdedir. Oluşturdugu kromoksit tabakası çelik yüzeyini film tabakası gibi kaplar ve korozyona karşı dayanıklılık sağlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Bir diğer adıyla 'manganez' doğada oksit durumunda bulunup demirle benzerlikler gösterir: nemli havada demir gibi paslanır.\nÇeliği sertleştirmek ve içindeki yabancı maddeleri temizlemek için çelik üretiminde kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Dünya yüzeyinde en yaygın dördüncü mineral ve yerkabuğunda en çok bulunan metaldir. Dövülmeye ve işlenmeye çok elverişli bir metalik elementtir.\nAna kullanım alanı yapı, inşaat ve ulaşım sektörüdür. Yapılarda betonun sağlamlığını artırmak için kullanılır. Demiryollarında da oldukça fazla miktarlarda kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Yaklaşık 982 °C'ye kadar sertliğini korur. jet motorları ve gaz türbinleri, manyetik çelikler ve bazı paslanmaz çelikler için alaşımlar yapmak için de kullanılır\nMavisi,yeşili, sarısı olarak bilinen bazı bileşikleri yüzyıllar boyunca porselen, cam, seramik, fayans ve emayeleri renklendirmek için kullanılmıştır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Doğada genelde kobalt ile birlikte bulunur.paslanmaz çelik üretiminde önemlidir. Doğal bir özelliği sayesinde manyetik alan içinde boyut değiştirme kabiliyetine sahiptir.\nPaslanmaz çelik, mıknatıs, bozuk para ve özel alaşımlar gibi birçok endüstriyel ürünlerde kullanılmakta \nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Gümüşten sonra en iyi iletken metal. Kablolarda, tellerde ve elektronik cihazların devre kartı yollarında sıklıkla kullanılır.\nAlışımları mücevherlerde ve madeni paralarda kullanılır. Bronz (tunç) üretmek için kalay ile alaşım yapılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Paslanmaya ve korozyona karşı korumak, demir, alüminyum gibi metalleri kaplamak için kullanılır. Otomotiv endüstrisinde, döküm kalıplarında, pil gövdelerinin yapımında kullanılır.\nBazı merhemlerin bileşiminde bulunur ve ince bir tabaka halinde uygulandığında cildin su kaybetmesini önler. Yazın güneş, kışın da soğuk yanıklarına karşı koruyucudur. \nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Oda sıcaklığında katı halde bulunur, yine oda sıcaklığında insan ile temasında erir. Elektronikte yarı iletken üretiminde kullanılır.\nLED'ler Ekranlar (ışık yayan diyotlar) ve GaAs lazer diyotlarının üretiminde yer alır.\nElement serisi : Metaller\nMaddenin hâli : Katı",
        "Elektronikte yarı iletkenlerde kullanılır: küçük miktarlarda fosfor, arsenik, galyum ve antimon ile kombine edildiğinde iyi bir yarı iletken haline gelir\nAyrıca alaşımlarda ve floresan lambalarda fosfor olarak da kullanılır. Kızılötesi radyasyona karşı şeffaflık özelliği ile kızılötesi optik aletler ve dedektörlerde kullanılır.\nElement serisi : Yarı metaller\nMaddenin hâli : Katı",
        "Normal sıcaklıkta katıyken 400 °C yaklaştığında gaz durumuna geçer, ölümcül derecede zehirlidir, fare, böcek zehirlerinde hatta kimyasal silahlarda da kullanılır.\nElektrik iletkenliğiyle elektronikte yarı iletkenlerde de kullanılır. Transistör yapmak için germanyuma az miktarda eklenir.\nElement serisi : Yarı metaller\nMaddenin hâli : Gaz",
        "Işığa maruz kaldığında elektrik direnci değişen bir elementtir. Güneş pillerinde, kameralarda ve diğer ışığın yoğunluğuna tepki veren cihazlarda sıklıkla kullanılır.\nAyrıca bir yarı iletkendir ve bazı katı-hal elektroniği ürünleriyle birlikte alternatif akımı doğru akıma dönüştüren cihazlarda da kullanılır.\nElement serisi : Ametaller\nMaddenin hâli : katı",
        "Zehirli ve pis kokulu, metalik olmayan tek elementtir. Tehlikelidir. Aşındırıcı ve çürütücüdür. Cilt temasında ciddi yanıklara neden olur ve buharı göz, burun ve boğazı tahriş eder.\nBileşikleri boyalarda, gaz dezenfektanlarda, aleve dayanıklı maddelerde, su arıtıcı bileşiklerde ve fotoğraf kimyasallarında kullanılır.\nElement serisi : Halojenler\nMaddenin hâli : Sıvı",
        "Genellikle aydınlatma ürünlerinde kullanılır. Fotoğrafçılıkta kullanılan bazı fotoğrafik flaşlarda, Akkor ampullerde inert dolgu gazı olarak kullanılır.\nFloresan lambalarda argonla karıştırılır. Hava alanı pistlerini gösteren yanıp sönen ışıklarda kullanılır, doldurulmuş tüpten akım geçirildiğinde mavimsi beyaz bir ışık elde edilir.",
        "Çok kolay iyonlaşması nedeniyle, iyon motorlu uzay araçlarında itici yakıt olarak kullanılabilme özelliğine sahiptir.\nÖzel camların yapımında, kalp araştırmalarında, vakum tüplerindeki gaz izlerini yok etmede ve fotosellerin yapımında da yaralanılır.\nElement serisi  :Alkali metaller\nMaddenin hâli : Katı",
        "Yumuşak ve dövülebilir yapılı, gümüşümsü sarı renkli metalik bir elementtir. Renkli televizyon görüntü tüplerinin üretiminde kullanılır.\nİşaret fişeklerinde ve havai fişeklerde kullanılır. Demirle birleştirilerek mıknatıs yapmak için kullanılır. Atom bombası patlamasının uzun ömürlü, radyoaktif bir serpinti ürünüdür.\nElement serisi : Alkalinler\nMaddenin hâli : Katı",
        "Bileşikleri ve alaşımlarının kullanıldığı bazı ürünler şunlardır; televizyon ekranları, lazerler, LCD ve LED ekran ve monitörler, enerji tasarruflu lambalar,\nOptik camlar, özel seramikler, ateşe dayanıklı tuğla, kamera ve fotoğraf makinesi mercekleri, floresan lambalar, tıbbi iğneler, yakıt hücreleri, elektrotlar, elektrolitler…\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Doğada az bulunan, korozyona dayanıklı bir metalik elementtir. Kolay bir şekilde nötron absorbe etmediği için nükleer reaktörlerde kullanılan element\nSağlık alanında yaygın olarak diş kaplamalarında. Korozyona ve Yüksek sıcaklıklara dayanıklılığıyla yüksek performanslı pompa, vanalarda, laboratuvar potalarında kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Parlak beyaz renkte, sünek ve yumuşak metalik bir elementtir. Eskiden kolombiyum (Cb) olarak da bilinen element\nNükleer reaktörler, jetler, füzeler için paslanmaz çelik alaşımlarda. Demir, nikel ile alaşım yapılır. Kalay, alüminyum, titanyum ve zirkonyum alaşımları süper iletken olarak bilinir.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Yüksek erime noktasına sahip 2617 °C de eriyen, sert, kırılgan gümüşümsü beyaz renkte metalik bir elementtir.\nUltra yüksek dayanıklı çelik alaşımlar yapmakta kullanılır. Alaşımları ısı ve korozyona dayanıklı hale getirir bu yönüyle uçaklarda, füzelerde, nükleer enerji sektöründe kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Molibdenin nötronlarla bombalanmasıyla üretilir. Yeryüzünde doğal olarak bulunmaz ancak spektral çizgilerinden yola çıkarak bazı yıldızlarda gözlenmiştir.\nsunî olarak elde edilen radyoaktif element. Nükleer tıpta kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Gümüş renginde, sert ve pürüzlü bir metaldir. Elektronik sektörü ve kimya endüstrisinde yaygın olarak kullanılır.\nÇok nadir bulunur, Üretimi de çok azdır. Platin cevherinden elde edilir. Nükleer silah testlerinde kullanılmıştır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Platin grubunda yer alan dünyanın en pahalı metallerinden biridir.Yansıma ve parlaklık oranı çok yüksek olduğu için özellikle pahalı takılarda kullanılır.\nEndüstride kullanılan önemli bir katalizördür. karakteristik olarak x-ray ışını üretir. Bu sebeple mamografi sistemlerinde kullanılabilen bir metaldir.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Platin grubu metallerdendir. Beyaz altının yapıtaşıdır ve bazen “beyaz altın” olarak adlandırılır. En belirgin özelliği; hidrojeni çok fazla emebilme ve depolayabilmesidir.\nCerrahi aletlerde, diş dolgu ve kuronlarında, elektrik kontaklarında ve yaylarda kullanılır. Saf metal olarak, analog kol saatleri için zemberek yapımında kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Değerli metalik elementlerin en önemlilerinden biridir. Altından sonra takı sektörünün en çok tercih edilen metal-gri renkte, paslanmayan, kolay işlenebilen değerli bir metal\nIsı ve elektrik iletkenliği çok iyidir, lehim, elektrik kontakları ve baskılı devre kartlarının yapımında kullanılır. Işığı en iyi yansıtan elementtir, ayna yapımında kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "En düşük erime noktasına sahip alaşımların önemli bir bileşenidir. bileşiklerinin çözeltileri zehirlidir. Sülfidi (CdS), sarı pigment olarak kullanılır.\nE.M.F. gözeleri ve lehim yapımında; ayrıca nötron yutucu özelliği nedeniyle nükleer reaktörlerde kontrol çubuklarında ve zırhlamada kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Çok yumuşaktır bu yüzden kolayca dövülebilir.metallerin erime noktasını düşürmede bir alaşım olarak kullanılır. Kimyasal özellikleri bakımından galyum ve talyuma benzer.\nLCD ekranlardan aynalara kadar kullanım alanı oldukça geniştir.% 24 bu element ve % 76 galyumdan oluşan bir alaşım oda sıcaklığında sıvı haldedir.\nElement serisi : Metaller\nMaddenin hâli : Katı",
        "Çelik konserve kutularının kaplama maddesidir. Ayrıca lehim, bronz, kalay ve kurşun alaşımlarında yer alır. Bazı diş macunlarının içeriğinde, bileşiği oln SnF5 kullanılır.\n Süperiletken mıknatısların yapımında da kullanılır. Saf element halinin kullanımı çok sınırlıdır.\nElement serisi : Zayıf metaller\nMaddenin hâli : Katı",
        "Mozart’ı öldüren madde olduğu iddia edilir. Kibritlerden mermilere, oyuncaklardan akülere kadar birçok üründe kullanılan bir elementtir.\nDemir alaşımlarını sertleştirmekte kullanılır. plastik ve çeşitli kimyasalların yapımında da kullanımı vardır.\nElement serisi: Yarı metal\nMaddenin hâli : Katı",
        "Bakırın ve paslanmaz çeliğin işlenebilirliğini artırır; demire katıldığındaysa dayanıklılığını artırarak, sülfürik asit nedenli aşınmanın etkisini azaltır.\nSeramik sanayinde, metal ürün üretiminde, camların boyanmasında, bateri zillerinde, pil kaplama koruyucularında, elektrik dirençlerinde ve termoelektrik aletlerde kullanılır.\nElemet serisi: Yarı Metal\nMaddenin Hali: Katı",
        "Bileşikleri, organik kimya ve eczacılık alanlarında çok önemlidir. Tıpta, tentürdiyot ve bu gibi mikrop kırıcılar da harici olarak kullanılır.\nYaşamın parçası olan elementler arasında önemli yer tutar. Dünyadaki zekâ geriliği vakaları bunun eksikliğine bağlanmaktadır.\nElement serisi : Halojenler\nMaddenin Hali: Katı",
        "Aydınlatma sektöründe çok sık kullanılan bir gazdır. Fotoğraf makinesi flaşları gibi anlık fotoğraf veya görüntü yakalama uygulamalarında çok etkili özellikler gösterir.\nYapılan bazı araştırmalarda, evreni bir arada tutan madde olarak kabul edilen “karanlık madde” araştırmalarında kullanılmaktadır.\nElement serisi : Soygazlar\nMaddenin hâli : Gaz",
        "Uzayabilen ve çok yumuşak bir metaldir. Tepkimeye çok istekli bir metaldir ve hemen hemen bütün elementlerle şiddetle veya alev çıkartarak tepkimeye girer.\n Oksijene karşı eğilimi yüksektir ve kolay iyonize olur. Bu nedenle de, roket motorlarında itici olarak kullanılır.\nElement serisi : Alkali metaller \nMaddenin hâli : Katı",
        "Beyaz-gri metalik rengindedir fakat yüksek reaktivitelikten dolayı element halinde bulunmaz. Hemen hemen bütün bileşikleri ise zehirlidir.\nMetalik Ba yakıldığında elma yeşili bir renk verir. Metalik halde saklanması çok zordur. Aktif bir element olduğu için su, hava ve asitlerle kolayca reaksiyon verir.\nElement serisi : Alkalinler\nMaddenin hâli : Katı",
        "",
        "Zirkonyum metalinin saflaştırılması sırasında elde edilir. Aşınmaya karşı olağanüstü derecede dayanıklı olan bu element, çok iyi nötron soğurabilme özelliği\nnedeniyle nükleer denizaltılardaki reaktör kontrol çubuklarında kullanılır. Vakum tüplerinde de gaz emici niteliğiyle bir gaz avcısı olarak kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Elektrolitik kapasitörlerin, vakum fırınlarının, kimyasal işlemlerde kullanılan aletlerin, nükleer reaktörlerin, hava taşıtlarının ve füze parçalarının yapımında kullanılır.\nVücut sıvılarının tamamına karşı dirençli olması nedeniyle, ameliyat gereçlerinin yapımında da tantal elementinden yararlanılır. \nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Diğer adıyla volfram, alaşımları, elektrik ampullerindeki ince tellerin, elektron ve televizyon tüplerinin, elektrikli fırınlarda sarımların ve ısıtıcı elemanların yapımında kullanılır.\nX-ışını hedeflerinde, hava taşıtlarında ve metal buharlaştırma işlemleri gibi yüksek sıcaklık gerektiren uygulamalarda da kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Kütle spektrograflarında ve iyon ölçüm aletlerinde bulunan ince tellerin yapımında kullanılır. Aşınmaya ve bozunmaya karşı dirençli olması nedeniyle,\nelektrik kontaklarında ve yüksek kaliteli bilimsel gereçlerin kaplamalarında kullanılır. Fotoğrafçılıkta kullanılan flaş ampullerinin yapımında da yararlanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "En büyük kullanım alanı, diğer metallerle çok sert alaşımların oluşturulmasıdır. Bu alaşımlar, çeşitli aletlerde kullanılan millerin, fonograf iğnelerinin,\ndolmakalem uçlarının ve benzeri aletlerin yapımında kullanılır. Parmak izi tesbitinde ve mikroskopla incelenmek üzere hazırlanan yağlı doku preparatlarının boyanmasında kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Esas olarak platini sertleştirici unsur olarak kullanılmasının yanı sıra, yüksek sıcaklıklara dayanıklı maddelerin yapımında da önemlidir.\nElektrik kontaklarında, özel saklama kaplarının yapımında, kansere karşı radyasyon tedavisinde, derialtı iğnelerinde ve helikopter bujilerinde kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Altından sonraki en kıymetli metaldir. Çelikten üç kat, mermerden ise 8 kat daha ağırdır ve paslanmaz elementtir\nKuyumculukta, laboratuar cihazlarında, elektrik kontaklarında, dişçilikte ve otomobil egzost kontrol cihazlarında kullanılır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Para olarak kullanılmış ve tarih boyunca en kıymetli metallerden sayılmıştır.Madeni para yapımında, kuyumculukta, dekorasyonda ve diş hekimliğinde kullanılır.\nDurağan olması ve kızılötesi ışığı iyi yansıtmasıyla, uzay uydularında kaplama olarak kullanılır. Kolay işlenebilirliği nedeniyle, elektronik endüstrisinde de kullanımı vardır.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Oda sıcaklığında sıvı halde bulunan 5 elementten birisidir. Altın ve gümüşü cevherlerden ayrıştırmak için kullanılır. Çok güçlü bir çözücüdür.\nTermometrelerin, barometrelerin, difüzyon pompalarının ve daha birçok laboratuvar gerecinin yapımında kullanılır. Zehirli ve pahalı bir maddedir.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Katı",
        "Metal olarak pek kullanım alanına sahip değildir. Bununla birlikte bazı bileşikleri özel nitelikli camların üretiminde ve fare zehiri yapımında kullanılır.\nBileşikleri düşük dozlarda bile insan için zehirleyici özelliğe sahiptir. Zehirlenme ölüm ya da kalıcı sinir sistemi bozukluklarına sebep olur.\nElement serisi : Zayıf metaller\nMaddenin hâli : Katı",
        "Ses titreşimlerini emici özelliği çok güçlü olan bu element, ses yalıtımında kullanılır. X-ışını ekipmanlarında ve nükleer santrallerde radyasyon kalkanı olarak işlev görür.\n Baz özelliği gösteren bir karbonat bileşiği olan ve benzeri diğer bileşikleri, boyaların yapısına katılır. Ancak, sağlık açısından olumsuz etkileri nedeniyle bu kullanımı azaltılmıştır.\nElement serisi : Metaller\nMaddenin hâli : Katı",
        "Katı hale geçerken %3,32 oranında genleşmek gibi özelliği vardır. Bu yüzden alaşımları, yüksek sıcaklıklardan zarar görebilecek malzemelerin yapısında kullanılmaya uygun.\nSoğudukça genleşme özelliğiyle, sıvı halde döküldükleri kapta soğuyup katı hale geçerken, kabın şeklini alırlar. Söndürücü güvenlik donanımlarının yapımında kullanılır.\nElement serisi : Zayıf metaller\nMaddenin hâli : Katı",
        "Uranyumdan 400 kat daha radyoaktif ve en tehlikeli radyasyon türü olan alfa radyoaktivite saçmaktadır. Pekblend cevherinin ayrıştırılmasıyla ortaya çıkmıştır.\nSanayide kullanılan ve sigarada bulunan ..., böbrek, karaciğer ve dalakta onarılamaz zarar yaratır. Çürümesi halinde büyük enerji ortaya çıkar. Bir gram'ı, 140 watt ısı enerjisi üretir.\nElement serisi : Yarı metaller\nMaddenin hâli : Katı",
        "Dünyada en az bulunan elementtir. Bu sebeple birçok özelliği tespit edilemediğinden gizemli bir element olarak görülüyor.\nHerhangi bir makroskopik numune ve radyoaktif ısınma ile hemen buharlaşacağı için incelenememiştir\nElement serisi : Halojenler\nMaddenin hâli : Katı",
        "Bazı hastanelerde radyasyon tedavilerinde ve bazı kanser türlerine karşı uygulanmaktadır. Deprem tahminlerinde de kullanılır.\nDoğal ortamlarda bulunabilir. Radyoaktifliği sebebiyle kanserojen etkisi vardır.\nElement serisi : Soygazlar\nMaddenin hâli : Gaz",
        "ismi Fransa’ya atfedilen, en son keşfedilen bir elementtir. Birçok özelliği henüz bilinmiyor. Dünyanın en nadir bulunan elementleri arasında ikinci sıradadır.\nÖyle ki, tüm yerkabuğunda bir bardağı dolduracak kadar olduğu öngörülüyor. Bu sebeple atom hızlandırıcılarda laboratuar ortamında yapay üretilebiliyor.\nElement serisi : Alkali metaller \nMaddenin hâli : Katı",
        "Uranyumdan 1 milyon kat daha fazla radyoaktivitesi olan bir element. İlk keşfedildiği yıllarda kendiliğinden ışık yayması sebebiyle adeta çığır açmış.\nSaat kadranlarının boyaları ve diş macunlarından çikolatalara kadar birçok üründe radyum kullanılmış. Hatta suya bile radyum katmışlar. \nBirçok garip hastalığın aniden ortaya çıkması ile de zararları araştırılmaya başlanmış.\nElement serisi : Alkalinler --- Maddenin hâli : Katı",
        "",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Geçiş metalleri\nMaddenin hâli : Bilinmiyor",
        "Havayla temas ettiği anda matlaşan ve kolay yanan bir metaldir. Hem elementin kendisi hem de bileşikleri orta düzeyde zehirlidir.\nStüdyo aydınlatmalarında ve projeksiyonda kullanılır. Özel optik camların yapımında kullanılır.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Katıldığı alaşımlara sıcaklığa karşı direnç kazandırır. Yanık ilaçlarında kullanılabilen bir elementtir.\nKeşfedildikten sonra ilk olarak gaz lambası gömleklerinde kullanılmıştır. Çakmaktaşlarında yüzde 50 oranında bulundurur.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Film stüdyolarında ışıklandırma ve projeksiyon amaçlı olarak kullanılır. Tuzları, cam ve emaye renklendirmede kullanılır.\nKaynakçıların kullandığı koruyucu gözlüklerde kullanılır. Cam yapımında çıkan ışığı filtreleme özelliğiyle, cam yapımcılarının koruyucu gözlüklerinde kullanılır.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "lazerler için yapay yakut yapımında, kaynakçı gözlüklerine takılan praseodimli özel cam üretiminde kullanılır.\nParlak mor cam ve kızılötesi radyasyonu filtreleyen özel cam üretmek içinde yararlanılır. Ayrıca bor ve demirle birlikte güçlü mıknatıs yapımında kullanılır.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Yapay olarak üretilen radyoaktif kimyasal bir element tir. Nükleer reaktörlerde üretilir. Beta ışıması yapar. Ve parlak materyallerin yapımında kullanılır.\nFosforla karıştırıldığı zaman ışığın fotoğral hücresine güç olarak kullanılır. Yansıttığı ışıklar zararsızdır. Ağır atomik elementlerle karıştığı zaman X Ray ışınları üretebilir.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Kalıcı mıknatıslarda kullanılan bir bileşendir. Nadir toprak elementleri ailesinin “nadir olmayan” üyeleri arasında yer alır.\nSinema endüstrisi aydınlatmaları ve kanser tedavisinde de yaygın olarak kullanılan bir elementtir.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Renkli televizyon ekranlarında gördüğümüz kırmızı rengin kaynağıdır. Fosforları, parlak bir kırmızı renk verir.\nEuro banknotlarında sahteciliği önlemek için ultraviyole ışını altında görülebilen bir ışık verir. Aynı zamanda grubundaki en reaktif elementtir. \nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Alışılagelmişin dışında süperiletken özellikler gösteren, ferromanyetik bir metaldir. Oda sıcaklığında da güçlü bir manyetizma gösterir.\nDemir, krom ve benzeri metal alaşımlara %1 oranında katıldığında; işlenebilirliği, ısıya ve oksidasyona dirençleri artmakta. Bileşikleri, televizyon renk maddesi olarak kullanılır.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Euro banknotları, tribolüminesans, yeşil fosforlar ve SoundBug hoparlörlerinin ortak noktası. Renkli televizyon tüplerinde yeşil fosforu uyaran maddeler arasındadır.\nAlışımları veya bileşikleri lazerler, x-ray ekranları, flüoresan lambalar, monitörler, katot ışını tüpleri, deniz sonar sistemleri, basınç sensörleri, cep telefonu ekranlarında kullanılır,\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Çelikten daha sert alaşımlarla kesilebilir ve aşırı ısınması engellendiği sürece kıvılcım çıkartmadan üzerinde çalışılabilir.\nGenelde deneysel amaçlar için kullanılır önemli kullanıma sahip değil. Ancak nötronları kolayca emdiği ve yüksek erime noktasına sahip olduğundan nükleer reaktörlerde kullanılır.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Olağandışı manyetik ve elektriksel özelliklere sahip bir elementtir. Gelecek vaat eden elementlerden biridir.\nHenüz ortada olmayan kuantum bilgisayarlarda şimdiden holmiyum kullanılabileceği belirtiliyor. Elementler arasında en yüksek manyetik momente sahip bir element\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Manyetik özellikleri sebebiyle fiber optik kablolar başta olmak üzere lazerlerde, çeşitli renklendirme uygulamalarında önemli bir metaldir.\nUygulandığı ürünlere pembe ve kırmızıya yakın tonlarda renk verir. Cerrahi lazerlerde etkin bir elementtir. Cilt hasarlarının onarılmasında kullanılan lazerlerin bir bileşenidir.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Bir bıçak ile kesilecek kadar yumuşaktır. Cerrahi lazerler başta olmak üzere sınırlı bazı uygulamalarda kullanılır.\nÖzellikle cilt sorunlarının tedavisinde kullanılan ... lazer, yanık izleri ve leke giderici olarak ideal bir lazer çeşididir.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Eğilip bükülebilecek kadar yumuşak olan bu element paslanmaz çeliğin dayanıklılığını, tanecik inceliğini\nve diğer mekanik özelliklerini iyileştirmede, metalürji ve kimya alanlarındaki deneylerde kullanılır.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Kanser tedavisi ve meteor yaşlarının tespiti gibi sınırlı alanda kullanılan nadir toprak elementidir yani lantanittir.\nEn ağır, en yoğun, en nadir ve en pahalı lantanit üyesidir. Üç farklı bilim adamı tarafından aynı yıllarda bağımsız olarak keşfedilen elementtir.\nElement serisi : Lantanitler\nMaddenin hali : Katı" ,
        "Aşırı derece radyoaktif element, karanlıkta mavi ışık saçar. Doğada az bulunması sebebiyle ticari kullanımı bulunmuyor.\nTıp ve uzay uygulamalarında kullanımı için araştırmalar devam ediyor. Nötron kaynağı olarak ve termoelektrik enerji üretiminde kullanılır.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Son yüzyılın en önemli stratejik hammaddelerinden biri olarak kabul ediliyor. Yerkabuğunda nadir bulunan, düşük radyoaktif bir metaldir.\nYoğunlaştırılmış bir yakıt olan toryum, diğer nükleer yakıtlara oranla daha çevreci bir nükleer enerji kaynağıdır.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "En nadir ve en pahalı elementtir. Doğal olarak uranyum cevherinden elde edilir. “Aktinyumun atası” olarak adını bu sözcükten almıştır\nBilinen bir kullanımı bulunmamaktadır.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Nükleer enerji ve atom bombası için kullanılan radyoaktif bir elementtir. Doğada saf uranyum bulunmaz, çeşitli elementler uranyum içerir.\nNükleer enerjinin hammaddesi, nükleer santrallerin yakıtı olan elementtir. Kolay elde edilemez, satılmaz. Nakliyesi sıkı kurallara tabidir. Kullanımı uluslararası anlaşmaları gerektirir.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "İleri teknoloji nükleer tesislerde üretilebilen, atom bombası üretiminde kullanılan elementlerin bir parçası olan radyoaktif elementtir.\nUranyumdan yapay olarak elde edilir. Uranyum ötesi (transuranyum) elementlerden biridir.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Dünyadaki en radyoaktif ve zehirli maddelerden biridir. Atom bombalarında ve nükleer enerji üretiminde kullanılır.\nDoğada çok nadir bulunduğu için nükleer reaktörlerde suni olarak elde edilir. Devasa enerji potansiyeli sebebiyle kitle imha silahı olarak kullanılmıştır. \nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Önemli bir alfa ve gama ışını kaynağıdır, duman dedektörlerinin ana bileşenidir.\nAdından da anlaşılacağı gibi Amerika kıtasını temsil eden element\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Sınırlı miktarlarda bulunabilmesi nedeniyle, çok az kullanım alanı vardır.\nMars seferinde kullanılan Alfa Proton X-ışını spektrometresinde, alfa parçacığı kaynağı olarak kullanılmıştır.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Özellikleriyle ilgili çok az şey biliniyor. Mevcut bilgilerin çoğu elementin periyodik tablodaki konumu temel alınarak tahmin edilen özelliklerdir.\nGünümüze kadar sadece 1 gram elde edilebilmiştir. Az sentezlenebildiği için deneysel verilerle, özellikleri tespit edilememiştir. Araştırmalar dışında kullanımı bulunmuyor.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Mikrogramı en az 60 dolar olan dünyanın en pahalı ikinci maddesidir. Doğada bulunmaz.Nükleer araştırmalarda, fisyon parçacıkları kaynağı olarak kullanılır.\nAltın ya da gümüş arama çalışmalarında, nötron kaynağı olarak da kullanımı vardır. Petrol kuyularında kullanılan nem ölçüm aygıtlarında da kaliforniyumdan yararlanılır.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Aktinitler\nMaddenin hâli : Katı",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Aktinitler\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Aktinitler\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Aktinitler\nMaddenin hâli : Bilinmiyor",
        "Süperağır Elementler\nRadyoaktiftirler, doğada doğal olarak bulunamazlar, Atomik araştırmalar dışında kullanılmazlar.\nElement serisi : Aktinitler\nMaddenin hâli : Bilinmiyor",
        ]

    cevap=["HİDROJEN","HELYUM","LİTYUM","BERİLYUM","BOR","KARBON","AZOT","OKSİJEN","FLOR","NEON","SODYUM","MAGNEZYUM","ALÜMİNYUM",
    "SİLİSYUM","FOSFOR","KÜKÜRT","KLOR","ARGON","POTASYUM","KALSİYUM","SKANDİYUM","TİTANYUM","VANADYUM","KROM","MANGAN","DEMİR",
    "KOBALT","NİKEL","BAKIR","ÇİNKO","GALYUM","GERMANYUM","ARSENİK","SELENYUM","BROM","KRİPTON","RUBİDYUM","STRONSİYUM","İTRİYUM",
    "ZİRKONYUM","NİYOBYUM","MOLİBDEN","TEKNESYUM","RUTENYUM","RODYUM","PALADYUM","GÜMÜŞ","KADMİYUM","İNDİYUM","KALAY","ANTİMON",
    "TELLÜR","İYOT","KSENON","SEZYUM","BARYUM","","HAFNİYUM","TANTAL","TUNGSTEN","RENYUM","OSMİYUM","İRİDYUM","PLATİN","ALTIN",
    "CIVA","TALYUM","KURŞUN","BİZMUT","POLONYUM","ASTATİN","RADON","FRANSİYUM","RADYUM","","","","","","","","","","","","","","",
    "","","LANTAN","SERYUM","PRASEODİM","NEODİM","PROMETYUM","SAMARYUM","EVROPİYUM","GADOLİNYUM","TERBİYUM","DİSPROSİYUM",
    "HOLMİYUM","ERBİYUM","TULYUM","İTERBİYUM","LUTESYUM","AKTİNYUM","TORYUM","PROTAKTİNYUM","URANYUM","NEPTÜNYUM","PLÜTONYUM","AMERİKYUM",
    "KÜRİYUM","BERKELYUM","KALİFORNİYUM","AYNŞTAYNYUM","FERMİYUM","MENDELEVYUM","NOBELYUM","LAVRENSİYUM"]