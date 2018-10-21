#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 hinha <hinha@parrot>
#
# Distributed under terms of the MIT license.

"""

"""
from time import sleep
from tqdm import tnrange, tqdm_notebook, tqdm
from abc import ABCMeta, abstractmethod
from random import randint

class Account(metaclass = ABCMeta):

    @abstractmethod
    def buatAkun(self):
        return 0

    def authenticate():
        return 0

    def penarikan():
        return 0

    def deposit():
        return 0

    def tampilkanSaldo():
        return 0

class SavingAccount(Account):

    def __init__(self):
        # [key][0] => nama ; [key][1] => saldo
        self.simpanAkun = {}
    
    def buatAkun(self, nama, awalDeposit):
        self.nomorAkun = randint(10000, 999999)
        self.simpanAkun[self.nomorAkun] = [nama, awalDeposit]
        print("Akun berhasil dibuat. Nomor akun: ", '\033[0;31m',self.nomorAkun, '\033[1;m')

    def authenticate(self, nama, noAkun):
        if nomorAkun in self.simpanAkun.keys():
            if self.simpanAkun[nomorAkun][0] == nama:
                print("Verifikasi berhasil!")
                return True
            else:
                print("Verifikasi gagal!")
                return False
        else:
            print("Verifikasi gagal!")
            return False

    def penarikan(self, jumlahPenarikan):
        if jumlahPenarikan > self.simpanAkun[self.nomorAkun][1]:
            print("Saldo tidak cukup")
        else:
            self.simpanAkun[self.nomorAkun][1] -= jumlahPenarikan
            print("Penarikan berhasil. Sisa saldo: ")
            self.tampilkanSaldo()

    def deposit(self, jumlahDeposit):
        self.simpanAkun[self.nomorAkun][1] += jumlahDeposit
        print("Deposit berhasil!. Sisa saldo: ")
        self.tampilkanSaldo()

    def tampilkanSaldo(self):
        print("Saldo anda: ", self.simpanAkun[self.nomorAkun][1])

    def jumlahAkun(self):
        for akun in self.simpanAkun:
            print(akun,end=" ")
            print(self.simpanAkun[self.nomorAkun][0], " ", self.simpanAkun[self.nomorAkun][1])


savingAkun = SavingAccount()

while True:
    print('''
    1. Buat akun
    2. Masuk sudah ada akun
    3. Keluar
          ''')
    menuUser = int(input("Enter: "))
    if menuUser is 1:
        nama = str(input("Masukkan nama anda: "))
        deposit = int(input("Masukkan jumlah deposit: "))
        print("\n")
        for i in tqdm(range(100)):
            sleep(0.10)        
        print("\n")
        savingAkun.buatAkun(nama, deposit)
    elif menuUser is 2:
        nama = str(input("Masukkan nama anda: "))
        nomorAkun = int(input("Nomor akun: "))
        print('\n')
        for i in tqdm(range(100)):
            sleep(0.10)        
        print("\n")
        verifStatus = savingAkun.authenticate(nama, nomorAkun)
        if verifStatus is True:
            while True:
                print("1. Penarikan")
                print("2. Deposit")
                print("3. cek Saldo")
                print("4. Kembali ke menu sebelumnya")
                menuUser = int(input("Enter: "))
                if menuUser is 1:
                    jumlahPenarikan = int(input("Jumlah penarikan: "))
                    savingAkun.penarikan(jumlahPenarikan)
                elif menuUser is 2:
                    jumlahDeposit = int(input("Jumlah Deposit: "))
                    savingAkun.deposit(jumlahDeposit)
                elif menuUser is 3:
                    savingAkun.tampilkanSaldo()
                else:
                    break
    elif menuUser is 99:
        savingAkun.jumlahAkun()
    elif menuUser is 3:
        exit()
                
