
.data
mesaj0:	.asciiz "**** Iki Pozitif Sayinin En Buyuk Ortak Bolenini Bulma ****\n"
mesaj1: .asciiz "Birinci Pozitif Sayiyi Giriniz (x)  : "
mesaj2: .asciiz "Ikinci Pozitif Sayiyi Giriniz  (y)  : "
mesaj3:	.asciiz "gcd(x,y)			      : "
mesaj4:	.asciiz "Devam Etmek Istermisiniz Evet(e)/Hayir(h): "
mesaj5:	.asciiz "Program Sonlanmistir ...\n"
newline: .asciiz "\n" 

x:	.word	0
y:	.word	0
sonuc:	.word	0

.text
.globl main
main:
	li $2,4
	la $4,mesaj0	
	syscall
geri:	
	
	li $2,4
	la $4,mesaj1 # x degeri istenir
	syscall
	
	li $2,5
	syscall
	
	la $3,x		# x adresi 3. registera yazilir
	sw $2,0($3)	#o adrese x degeri yazilir
	li $2,4
	la $4,mesaj2
	syscall
	
	li $2,5
	syscall
	
	la $3,y		# y adresi 3. registera yazilir
	sw $2,0($3)	#o  adrese y degeri yazilir
	li $2,4
	la $4,mesaj3
	syscall
	
	jal gcd	# x y alindiktan sonra gcd ye yollanir
	
	li $2,4
	la $4,newline
	syscall
	
	li $2,4
	la $4,mesaj4	#devam etmek ister misin sorulur
	syscall
	
	li $2,12
	syscall
	
	sw $2,0($3)  # verilen cevap 3.register a yazilir
	
	li $2,4
	la $4,newline
	syscall
	
	lw $13,0($3)	#3.registerdaki cevap okunup 13 e yazilir
	li $14,101 	# 101 e nin makine dilinde karsiligi 
	beq $13,$14,geri 	# cevap e ise geriye yollaniyor
		
	li $2,4
	la $4,mesaj5	# hayir ise bitiriliyor ekrana bastirilir
	syscall
		
	li $v0,10
	syscall
 
gcd:
	lw $10,x
	lw $11,y
	ilk_if:
		  beqz $10,return_y
		  bnez $11,while 
		  la $3,sonuc	# y 0 olması durumunda x bastirilir
		  sw $10,0($3)	# burada sonuca x nin degerini 	
		  li $2,1	 	#atayip
		  move $4,$10	# x i ekrana bastırıyoruz
		  syscall
		  jr $31
	
	while:
		if: ble $10,$11,else
		sub $10,$10,$11  #x-y islemi yapip 
		b ilk_if		 # ilk_if e gönderilir
		
		else: sub $11,$11,$10	#y-x islemi yapilir
		b ilk_if
			
	return_y:
		la $3,sonuc	# x 0 olması durumunda y bastirilir
		sw $11,0($3)	# burada sonuca y nin degerini 	
		li $2,1		#atayip	
		move $4,$11	# y yi ekrana bastırıyoruz
		syscall
		jr $31
	
