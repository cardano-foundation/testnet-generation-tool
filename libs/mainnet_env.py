binary = '''{
  "version": "10.2.1",
  "url": "https://github.com/IntersectMBO/cardano-node/releases/download/10.2.1/cardano-node-10.2.1-linux.tar.gz"
}'''


byron = '''{
    "avvmDistr": {},
    "blockVersionData": {
        "heavyDelThd": "300000000000",
        "maxBlockSize": "2000000",
        "maxHeaderSize": "2000000",
        "maxProposalSize": "700",
        "maxTxSize": "4096",
        "mpcThd": "20000000000000",
        "scriptVersion": 0,
        "slotDuration": "20000",
        "softforkRule": {
            "initThd": "900000000000000",
            "minThd": "600000000000000",
            "thdDecrement": "50000000000000"
        },
        "txFeePolicy": {
            "multiplier": "43946000000",
            "summand": "155381000000000"
        },
        "unlockStakeEpoch": "18446744073709551615",
        "updateImplicit": "10000",
        "updateProposalThd": "100000000000000",
        "updateVoteThd": "1000000000000"
    },
    "ftsSeed": "76617361206f7061736120736b6f766f726f64612047677572646120626f726f64612070726f766f6461",
    "protocolConsts": {
        "k": 2160,
        "protocolMagic": 764824073,
        "vssMaxTTL": 6,
        "vssMinTTL": 2
    },
    "startTime": 1506203091,
    "bootStakeholders": {
        "1deb82908402c7ee3efeb16f369d97fba316ee621d09b32b8969e54b": 1,
        "65904a89e6d0e5f881513d1736945e051b76f095eca138ee869d543d": 1,
        "5411c7bf87c252609831a337a713e4859668cba7bba70a9c3ef7c398": 1,

        "6c9e14978b9d6629b8703f4f25e9df6ed4814b930b8403b0d45350ea": 1,
        "43011479a595b300e0726910d0b602ffcdd20466a3b8ceeacd3fbc26": 1,

        "5071d8802ddd05c59f4db907bd1749e82e6242caf6512b20a8368fcf": 1,
        "af2800c124e599d6dec188a75f8bfde397ebb778163a18240371f2d1": 1
    },
    "heavyDelegation": {
        "1deb82908402c7ee3efeb16f369d97fba316ee621d09b32b8969e54b":{"cert":"c8b39f094dc00608acb2d20ff274cb3e0c022ccb0ce558ea7c1a2d3a32cd54b42cc30d32406bcfbb7f2f86d05d2032848be15b178e3ad776f8b1bc56a671400d","delegatePk":"6MA6A8Cy3b6kGVyvOfQeZp99JR7PIh+7LydcCl1+BdGQ3MJG9WyOM6wANwZuL2ZN2qmF6lKECCZDMI3eT1v+3w==","issuerPk":"UHMxYf2vtsjLb64OJb35VVEFs2eO+wjxd1uekN5PXHe8yM7/+NkBHLJ4so/dyG2bqwmWVtd6eFbHYZEIy/ZXUg==","omega":0},
        "65904a89e6d0e5f881513d1736945e051b76f095eca138ee869d543d":{"cert":"552741f728196e62f218047b944b24ce4d374300d04b9b281426f55aa000d53ded66989ad5ea0908e6ff6492001ff18ece6c7040a934060759e9ae09863bf203","delegatePk":"X93u2t4nFNbbL54RBHQ9LY2Bjs3cMG4XYQjbFMqt1EG0V9WEDGD4hAuZyPeMKQriKdT4Qx5ni6elRcNWB7lN2w==","issuerPk":"C9sfXvPZlAN1k/ImYlXxNKVkZYuy34FLO5zvuW2jT6nIiFkchbdw/TZybV89mRxmiCiv/Hu+CHL9aZE25mTZ2A==","omega":0},
        "5411c7bf87c252609831a337a713e4859668cba7bba70a9c3ef7c398":{"cert":"c946fd596bdb31949aa435390de19a549c9698cad1813e34ff2431bc06190188188f4e84001380713e3f916c7526096e7c4855904bff40385007b81e1e657d0e","delegatePk":"i1Mgdin5ow5LIBUETzN8AXNavmckPBlHDJ2ujHtzJ5gJiHufQg1vcO4enVDBYFKHjlRLZctdRL1pF1ayhM2Cmw==","issuerPk":"mm+jQ8jGw23ho1Vv60Eb/fhwjVr4jehibQ/Gv6Tuu22Zq4PZDWZTGtkSLT+ctLydBbJkSGclMqaNp5b5MoQx/Q==","omega":0},

        "6c9e14978b9d6629b8703f4f25e9df6ed4814b930b8403b0d45350ea":{"cert":"8ab43e904b06e799c1817c5ced4f3a7bbe15cdbf422dea9d2d5dc2c6105ce2f4d4c71e5d4779f6c44b770a133636109949e1f7786acb5a732bcdea0470fea406","delegatePk":"8U9xLcYA15MFLUhC1QzvpOZYhOps+DcHB564zjAu/IXa6SLV6zg40rkXhPBIJNJnZ7+2W9NqNudP7EbQnZiFjQ==","issuerPk":"JlZuhvxrmxd8hIDidbKxErVz9tBz+d7qU7jZnE7ZdrM1srOELw44AAHwkLySPKqWke2RFeKG2pQh4nRcesyH8Q==","omega":0},
        "43011479a595b300e0726910d0b602ffcdd20466a3b8ceeacd3fbc26":{"cert":"cf6ddc111545f61c2442b68bd7864ea952c428d145438948ef48a4af7e3f49b175564007685be5ae3c9ece0ab27de09721db0cb63aa67dc081a9f82d7e84210d","delegatePk":"kYDYGOac2ZfjRmPEGKZIwHby4ZzUGU5IbhWdhYC8bNqBNERAxq0OUwb9A1vvkoHaXY+9OPWfWI9wgQFu5hET0g==","issuerPk":"0pZchpkBIxeYxdAtOfyip5qkfD6FSSG1hVyC/RRwiRUX4fp3FlXsjK0T7PblcZrcU5L8BX4XA9X1gzEeg3Ri8Q==","omega":0},

        "5071d8802ddd05c59f4db907bd1749e82e6242caf6512b20a8368fcf":{"cert":"496b29b5c57e8ac7cffc6e8b5e40b3d260e407ad4d09792decb0a22d54da7f8828265688a18aa1a5c76d9e7477a5f4a650501409fdcd3855b300fd2e2bc3c605","delegatePk":"icKfjErye3rMvliXR4IBNOu6ocrzzpSScKPQx9z9VBsd7zJtLvDbeANByeJh8EiQze7x+cmfbZC47cp9PPwJiA==","issuerPk":"mTqPBW0tPlCwrGATnxDfj4Ej1ffEgXtA2sK13YqpSoLoU2gy5jEt38B4fXtTEMgVZVraT9vPaxIpfURY7Mwt+w==","omega":0},
        "af2800c124e599d6dec188a75f8bfde397ebb778163a18240371f2d1":{"cert":"e03e62f083df5576360e60a32e22bbb07b3c8df4fcab8079f1d6f61af3954d242ba8a06516c395939f24096f3df14e103a7d9c2b80a68a9363cf1f27c7a4e307","delegatePk":"YSYalbdhPua/IGfa13twNJcpsMUNV7wc8w3g20oec6iF0AVK98I/xsN5GdukHGAqV+LQ+TKaeVS4ZzONb7LJRQ==","issuerPk":"G8l6L+AsKXiAzo7P2Zf+TB7AnuEP7u6faGdgFmsFKB1ig0aP/ZO+ywyVbM3dZC35sSRMkVkRGF+kk1X28iv6uQ==","omega":0}
    },
    "nonAvvmBalances": {},
    "vssCerts": {
        "6bef444609d6e336cb1fe1daba278918dbc5768e6754c2945dd8d25c":{"expiryEpoch":5,"signature":"2d96e4d4a4c506cc5762128b814ffb20afb97d30eb976334cd241a3935bd155ea1d68772b0903bde4584470359206769d83fa2ce55f56a1027ec3c52cb5e8703","signingKey":"6MA6A8Cy3b6kGVyvOfQeZp99JR7PIh+7LydcCl1+BdGQ3MJG9WyOM6wANwZuL2ZN2qmF6lKECCZDMI3eT1v+3w==","vssKey":"WCED6k6ArqOnhQtfNRg0FSCxWmAtocZcyV33AdjMotjGwxI="},
        "eb649333a196ecb024a4a5919d3ce86084014136fd3e884e52ecd057":{"expiryEpoch":5,"signature":"0b115a39935ce6008a4bbad0377f35463fd3510e282186ba43492768a02eb000bd4d3bc50799a24c53879ff2f2587179e797ee1c312acaf107cba67f91cb280b","signingKey":"X93u2t4nFNbbL54RBHQ9LY2Bjs3cMG4XYQjbFMqt1EG0V9WEDGD4hAuZyPeMKQriKdT4Qx5ni6elRcNWB7lN2w==","vssKey":"WCECS11PWxybUHKY2hHmBgm/zYaR2YsqsH+f3uPOp2ydz/E="},
        "5ffca3a329599727e39a7472c5270e54cf59a27b74306cc9f7fd0f5e":{"expiryEpoch":5,"signature":"6cc8d84dd55b41efcf46c4b3086da1fb60c938182b4b66657650839d9fac1e2194a8253dc6d5c107ac0e9e714d1364fff9d2114eae07363d9937ee1d92b69c06","signingKey":"i1Mgdin5ow5LIBUETzN8AXNavmckPBlHDJ2ujHtzJ5gJiHufQg1vcO4enVDBYFKHjlRLZctdRL1pF1ayhM2Cmw==","vssKey":"WCEDca27BxibVjQoA1QJaWx4gAE2MUB0lHfb6jJ3iorXD7s="},
        "ce1e50f578d3043dc78d8777f5723cc7b6ca512d8cdbe8a09aafc9c3":{"expiryEpoch":5,"signature":"2b830f1a79d2baca791a90c3784d74ec9f00267efac5ccd3cd7082b854234f411c237b59f34736933ba626fadc87fd6b2114c44486de692892d7401343990e01","signingKey":"8U9xLcYA15MFLUhC1QzvpOZYhOps+DcHB564zjAu/IXa6SLV6zg40rkXhPBIJNJnZ7+2W9NqNudP7EbQnZiFjQ==","vssKey":"WCECs1+lg8Lsm15FxfY8bhGyRuwe8yOaSH0wwSajLRYeW/s="},
        "0efd6f3b2849d5baf25b3e2bf2d46f88427b4e455fc3dc43f57819c5":{"expiryEpoch":5,"signature":"d381d32a18cd12a1c6ff87da0229c9a5b998fd093ac29f5d932bfc918e7dbc6e1dc292a36c46a3e129c5b1ef661124361426b443480534ff51dacc82bf4b630f","signingKey":"kYDYGOac2ZfjRmPEGKZIwHby4ZzUGU5IbhWdhYC8bNqBNERAxq0OUwb9A1vvkoHaXY+9OPWfWI9wgQFu5hET0g==","vssKey":"WCECgow+hJK+BxjNx0gIYrap+onUsRocObQEVzvJsdj68vw="},
        "1040655f58d5bf2be1c06f983abf66c7f01d28c239f27648a0c73e5d":{"expiryEpoch":5,"signature":"b02e89abb183da7c871bca87a563d38356b44f403348b6a5f24ee4459335290d980db69a6482455aae231a9880defe2fd4212272c4b2ea3da8744a8ba750440a","signingKey":"icKfjErye3rMvliXR4IBNOu6ocrzzpSScKPQx9z9VBsd7zJtLvDbeANByeJh8EiQze7x+cmfbZC47cp9PPwJiA==","vssKey":"WCECQoZjWJSu/6R74CC0ueh7cXmR0sasmTuCqf8X0BtAQ4o="},
        "1fa56ba63cff50d124b6af42f33b245a30fcd1b0170d7704b0b201c7":{"expiryEpoch":5,"signature":"7bb244c4fa1499021b0f2d36515a1f288a33cf00f1b88b57626998b439dcfb03ad88a7bc93101e4d83cdc75329799fbb2ccb28a7212a3e49737b06287d09b00c","signingKey":"YSYalbdhPua/IGfa13twNJcpsMUNV7wc8w3g20oec6iF0AVK98I/xsN5GdukHGAqV+LQ+TKaeVS4ZzONb7LJRQ==","vssKey":"WCECNXeQRqiTZSPDDyeRJ3gl/QzYMLLtNH0yN+XOl17pu8Y="}
    }
}'''

shelley = '''{
  "activeSlotsCoeff": 0.05,
  "protocolParams": {
    "protocolVersion": {
      "minor": 0,
      "major": 2
    },
    "decentralisationParam": 1,
    "eMax": 18,
    "extraEntropy": {
      "tag": "NeutralNonce"
    },
    "maxTxSize": 16384,
    "maxBlockBodySize": 65536,
    "maxBlockHeaderSize": 1100,
    "minFeeA": 44,
    "minFeeB": 155381,
    "minUTxOValue": 1000000,
    "poolDeposit": 500000000,
    "minPoolCost": 340000000,
    "keyDeposit": 2000000,
    "nOpt": 150,
    "rho": 0.003,
    "tau": 0.20,
    "a0": 0.3
  },
  "genDelegs": {
    "ad5463153dc3d24b9ff133e46136028bdc1edbb897f5a7cf1b37950c": {
      "delegate": "d9e5c76ad5ee778960804094a389f0b546b5c2b140a62f8ec43ea54d",
      "vrf": "64fa87e8b29a5b7bfbd6795677e3e878c505bc4a3649485d366b50abadec92d7"
    },
    "b9547b8a57656539a8d9bc42c008e38d9c8bd9c8adbb1e73ad529497": {
      "delegate": "855d6fc1e54274e331e34478eeac8d060b0b90c1f9e8a2b01167c048",
      "vrf": "66d5167a1f426bd1adcc8bbf4b88c280d38c148d135cb41e3f5a39f948ad7fcc"
    },
    "60baee25cbc90047e83fd01e1e57dc0b06d3d0cb150d0ab40bbfead1": {
      "delegate": "7f72a1826ae3b279782ab2bc582d0d2958de65bd86b2c4f82d8ba956",
      "vrf": "c0546d9aa5740afd569d3c2d9c412595cd60822bb6d9a4e8ce6c43d12bd0f674"
    },
    "f7b341c14cd58fca4195a9b278cce1ef402dc0e06deb77e543cd1757": {
      "delegate": "69ae12f9e45c0c9122356c8e624b1fbbed6c22a2e3b4358cf0cb5011",
      "vrf": "6394a632af51a32768a6f12dac3485d9c0712d0b54e3f389f355385762a478f2"
    },
    "162f94554ac8c225383a2248c245659eda870eaa82d0ef25fc7dcd82": {
      "delegate": "4485708022839a7b9b8b639a939c85ec0ed6999b5b6dc651b03c43f6",
      "vrf": "aba81e764b71006c515986bf7b37a72fbb5554f78e6775f08e384dbd572a4b32"
    },
    "2075a095b3c844a29c24317a94a643ab8e22d54a3a3a72a420260af6": {
      "delegate": "6535db26347283990a252313a7903a45e3526ec25ddba381c071b25b",
      "vrf": "fcaca997b8105bd860876348fc2c6e68b13607f9bbd23515cd2193b555d267af"
    },
    "268cfc0b89e910ead22e0ade91493d8212f53f3e2164b2e4bef0819b": {
      "delegate": "1d4f2e1fda43070d71bb22a5522f86943c7c18aeb4fa47a362c27e23",
      "vrf": "63ef48bc5355f3e7973100c371d6a095251c80ceb40559f4750aa7014a6fb6db"
    }
  },
  "updateQuorum": 5,
  "networkId": "Mainnet",
  "initialFunds": {},
  "maxLovelaceSupply": 45000000000000000,
  "networkMagic": 764824073,
  "epochLength": 432000,
  "systemStart": "2017-09-23T21:44:51Z",
  "slotsPerKESPeriod": 129600,
  "slotLength": 1,
  "maxKESEvolutions": 62,
  "securityParam": 2160
}'''

alonzo = '''{
    "lovelacePerUTxOWord": 34482,
    "executionPrices": {
        "prSteps":
    {
        "numerator" :   721,
        "denominator" : 10000000
        },
        "prMem":
    {
        "numerator" :   577,
        "denominator" : 10000
    }
    },
    "maxTxExUnits": {
        "exUnitsMem":   10000000,
        "exUnitsSteps": 10000000000
    },
    "maxBlockExUnits": {
        "exUnitsMem":   50000000,
        "exUnitsSteps": 40000000000
    },
    "maxValueSize": 5000,
    "collateralPercentage": 150,
    "maxCollateralInputs": 3,
    "costModels": {
        "PlutusV1": {
            "sha2_256-memory-arguments": 4,
            "equalsString-cpu-arguments-constant": 1000,
            "cekDelayCost-exBudgetMemory": 100,
            "lessThanEqualsByteString-cpu-arguments-intercept": 103599,
            "divideInteger-memory-arguments-minimum": 1,
            "appendByteString-cpu-arguments-slope": 621,
            "blake2b-cpu-arguments-slope": 29175,
            "iData-cpu-arguments": 150000,
            "encodeUtf8-cpu-arguments-slope": 1000,
            "unBData-cpu-arguments": 150000,
            "multiplyInteger-cpu-arguments-intercept": 61516,
            "cekConstCost-exBudgetMemory": 100,
            "nullList-cpu-arguments": 150000,
            "equalsString-cpu-arguments-intercept": 150000,
            "trace-cpu-arguments": 150000,
            "mkNilData-memory-arguments": 32,
            "lengthOfByteString-cpu-arguments": 150000,
            "cekBuiltinCost-exBudgetCPU": 29773,
            "bData-cpu-arguments": 150000,
            "subtractInteger-cpu-arguments-slope": 0,
            "unIData-cpu-arguments": 150000,
            "consByteString-memory-arguments-intercept": 0,
            "divideInteger-memory-arguments-slope": 1,
            "divideInteger-cpu-arguments-model-arguments-slope": 118,
            "listData-cpu-arguments": 150000,
            "headList-cpu-arguments": 150000,
            "chooseData-memory-arguments": 32,
            "equalsInteger-cpu-arguments-intercept": 136542,
            "sha3_256-cpu-arguments-slope": 82363,
            "sliceByteString-cpu-arguments-slope": 5000,
            "unMapData-cpu-arguments": 150000,
            "lessThanInteger-cpu-arguments-intercept": 179690,
            "mkCons-cpu-arguments": 150000,
            "appendString-memory-arguments-intercept": 0,
            "modInteger-cpu-arguments-model-arguments-slope": 118,
            "ifThenElse-cpu-arguments": 1,
            "mkNilPairData-cpu-arguments": 150000,
            "lessThanEqualsInteger-cpu-arguments-intercept": 145276,
            "addInteger-memory-arguments-slope": 1,
            "chooseList-memory-arguments": 32,
            "constrData-memory-arguments": 32,
            "decodeUtf8-cpu-arguments-intercept": 150000,
            "equalsData-memory-arguments": 1,
            "subtractInteger-memory-arguments-slope": 1,
            "appendByteString-memory-arguments-intercept": 0,
            "lengthOfByteString-memory-arguments": 4,
            "headList-memory-arguments": 32,
            "listData-memory-arguments": 32,
            "consByteString-cpu-arguments-intercept": 150000,
            "unIData-memory-arguments": 32,
            "remainderInteger-memory-arguments-minimum": 1,
            "bData-memory-arguments": 32,
            "lessThanByteString-cpu-arguments-slope": 248,
            "encodeUtf8-memory-arguments-intercept": 0,
            "cekStartupCost-exBudgetCPU": 100,
            "multiplyInteger-memory-arguments-intercept": 0,
            "unListData-memory-arguments": 32,
            "remainderInteger-cpu-arguments-model-arguments-slope": 118,
            "cekVarCost-exBudgetCPU": 29773,
            "remainderInteger-memory-arguments-slope": 1,
            "cekForceCost-exBudgetCPU": 29773,
            "sha2_256-cpu-arguments-slope": 29175,
            "equalsInteger-memory-arguments": 1,
            "indexByteString-memory-arguments": 1,
            "addInteger-memory-arguments-intercept": 1,
            "chooseUnit-cpu-arguments": 150000,
            "sndPair-cpu-arguments": 150000,
            "cekLamCost-exBudgetCPU": 29773,
            "fstPair-cpu-arguments": 150000,
            "quotientInteger-memory-arguments-minimum": 1,
            "decodeUtf8-cpu-arguments-slope": 1000,
            "lessThanInteger-memory-arguments": 1,
            "lessThanEqualsInteger-cpu-arguments-slope": 1366,
            "fstPair-memory-arguments": 32,
            "modInteger-memory-arguments-intercept": 0,
            "unConstrData-cpu-arguments": 150000,
            "lessThanEqualsInteger-memory-arguments": 1,
            "chooseUnit-memory-arguments": 32,
            "sndPair-memory-arguments": 32,
            "addInteger-cpu-arguments-intercept": 197209,
            "decodeUtf8-memory-arguments-slope": 8,
            "equalsData-cpu-arguments-intercept": 150000,
            "mapData-cpu-arguments": 150000,
            "mkPairData-cpu-arguments": 150000,
            "quotientInteger-cpu-arguments-constant": 148000,
            "consByteString-memory-arguments-slope": 1,
            "cekVarCost-exBudgetMemory": 100,
            "indexByteString-cpu-arguments": 150000,
            "unListData-cpu-arguments": 150000,
            "equalsInteger-cpu-arguments-slope": 1326,
            "cekStartupCost-exBudgetMemory": 100,
            "subtractInteger-cpu-arguments-intercept": 197209,
            "divideInteger-cpu-arguments-model-arguments-intercept": 425507,
            "divideInteger-memory-arguments-intercept": 0,
            "cekForceCost-exBudgetMemory": 100,
            "blake2b-cpu-arguments-intercept": 2477736,
            "remainderInteger-cpu-arguments-constant": 148000,
            "tailList-cpu-arguments": 150000,
            "encodeUtf8-cpu-arguments-intercept": 150000,
            "equalsString-cpu-arguments-slope": 1000,
            "lessThanByteString-memory-arguments": 1,
            "multiplyInteger-cpu-arguments-slope": 11218,
            "appendByteString-cpu-arguments-intercept": 396231,
            "lessThanEqualsByteString-cpu-arguments-slope": 248,
            "modInteger-memory-arguments-slope": 1,
            "addInteger-cpu-arguments-slope": 0,
            "equalsData-cpu-arguments-slope": 10000,
            "decodeUtf8-memory-arguments-intercept": 0,
            "chooseList-cpu-arguments": 150000,
            "constrData-cpu-arguments": 150000,
            "equalsByteString-memory-arguments": 1,
            "cekApplyCost-exBudgetCPU": 29773,
            "quotientInteger-memory-arguments-slope": 1,
            "verifySignature-cpu-arguments-intercept": 3345831,
            "unMapData-memory-arguments": 32,
            "mkCons-memory-arguments": 32,
            "sliceByteString-memory-arguments-slope": 1,
            "sha3_256-memory-arguments": 4,
            "ifThenElse-memory-arguments": 1,
            "mkNilPairData-memory-arguments": 32,
            "equalsByteString-cpu-arguments-slope": 247,
            "appendString-cpu-arguments-intercept": 150000,
            "quotientInteger-cpu-arguments-model-arguments-slope": 118,
            "cekApplyCost-exBudgetMemory": 100,
            "equalsString-memory-arguments": 1,
            "multiplyInteger-memory-arguments-slope": 1,
            "cekBuiltinCost-exBudgetMemory": 100,
            "remainderInteger-memory-arguments-intercept": 0,
            "sha2_256-cpu-arguments-intercept": 2477736,
            "remainderInteger-cpu-arguments-model-arguments-intercept": 425507,
            "lessThanEqualsByteString-memory-arguments": 1,
            "tailList-memory-arguments": 32,
            "mkNilData-cpu-arguments": 150000,
            "chooseData-cpu-arguments": 150000,
            "unBData-memory-arguments": 32,
            "blake2b-memory-arguments": 4,
            "iData-memory-arguments": 32,
            "nullList-memory-arguments": 32,
            "cekDelayCost-exBudgetCPU": 29773,
            "subtractInteger-memory-arguments-intercept": 1,
            "lessThanByteString-cpu-arguments-intercept": 103599,
            "consByteString-cpu-arguments-slope": 1000,
            "appendByteString-memory-arguments-slope": 1,
            "trace-memory-arguments": 32,
            "divideInteger-cpu-arguments-constant": 148000,
            "cekConstCost-exBudgetCPU": 29773,
            "encodeUtf8-memory-arguments-slope": 8,
            "quotientInteger-cpu-arguments-model-arguments-intercept": 425507,
            "mapData-memory-arguments": 32,
            "appendString-cpu-arguments-slope": 1000,
            "modInteger-cpu-arguments-constant": 148000,
            "verifySignature-cpu-arguments-slope": 1,
            "unConstrData-memory-arguments": 32,
            "quotientInteger-memory-arguments-intercept": 0,
            "equalsByteString-cpu-arguments-constant": 150000,
            "sliceByteString-memory-arguments-intercept": 0,
            "mkPairData-memory-arguments": 32,
            "equalsByteString-cpu-arguments-intercept": 112536,
            "appendString-memory-arguments-slope": 1,
            "lessThanInteger-cpu-arguments-slope": 497,
            "modInteger-cpu-arguments-model-arguments-intercept": 425507,
            "modInteger-memory-arguments-minimum": 1,
            "sha3_256-cpu-arguments-intercept": 0,
            "verifySignature-memory-arguments": 1,
            "cekLamCost-exBudgetMemory": 100,
            "sliceByteString-cpu-arguments-intercept": 150000
        }
    }
}'''

conway = '''{
  "poolVotingThresholds": {
    "committeeNormal": 0.51,
    "committeeNoConfidence": 0.51,
    "hardForkInitiation": 0.51,
    "motionNoConfidence": 0.51,
    "ppSecurityGroup": 0.51
  },
  "dRepVotingThresholds": {
    "motionNoConfidence": 0.67,
    "committeeNormal": 0.67,
    "committeeNoConfidence": 0.6,
    "updateToConstitution": 0.75,
    "hardForkInitiation": 0.6,
    "ppNetworkGroup": 0.67,
    "ppEconomicGroup": 0.67,
    "ppTechnicalGroup": 0.67,
    "ppGovGroup": 0.75,
    "treasuryWithdrawal": 0.67
  },
  "committeeMinSize": 7,
  "committeeMaxTermLength": 146,
  "govActionLifetime": 6,
  "govActionDeposit": 100000000000,
  "dRepDeposit": 500000000,
  "dRepActivity": 20,
  "minFeeRefScriptCostPerByte": 15,
  "plutusV3CostModel": [
    100788,
    420,
    1,
    1,
    1000,
    173,
    0,
    1,
    1000,
    59957,
    4,
    1,
    11183,
    32,
    201305,
    8356,
    4,
    16000,
    100,
    16000,
    100,
    16000,
    100,
    16000,
    100,
    16000,
    100,
    16000,
    100,
    100,
    100,
    16000,
    100,
    94375,
    32,
    132994,
    32,
    61462,
    4,
    72010,
    178,
    0,
    1,
    22151,
    32,
    91189,
    769,
    4,
    2,
    85848,
    123203,
    7305,
    -900,
    1716,
    549,
    57,
    85848,
    0,
    1,
    1,
    1000,
    42921,
    4,
    2,
    24548,
    29498,
    38,
    1,
    898148,
    27279,
    1,
    51775,
    558,
    1,
    39184,
    1000,
    60594,
    1,
    141895,
    32,
    83150,
    32,
    15299,
    32,
    76049,
    1,
    13169,
    4,
    22100,
    10,
    28999,
    74,
    1,
    28999,
    74,
    1,
    43285,
    552,
    1,
    44749,
    541,
    1,
    33852,
    32,
    68246,
    32,
    72362,
    32,
    7243,
    32,
    7391,
    32,
    11546,
    32,
    85848,
    123203,
    7305,
    -900,
    1716,
    549,
    57,
    85848,
    0,
    1,
    90434,
    519,
    0,
    1,
    74433,
    32,
    85848,
    123203,
    7305,
    -900,
    1716,
    549,
    57,
    85848,
    0,
    1,
    1,
    85848,
    123203,
    7305,
    -900,
    1716,
    549,
    57,
    85848,
    0,
    1,
    955506,
    213312,
    0,
    2,
    270652,
    22588,
    4,
    1457325,
    64566,
    4,
    20467,
    1,
    4,
    0,
    141992,
    32,
    100788,
    420,
    1,
    1,
    81663,
    32,
    59498,
    32,
    20142,
    32,
    24588,
    32,
    20744,
    32,
    25933,
    32,
    24623,
    32,
    43053543,
    10,
    53384111,
    14333,
    10,
    43574283,
    26308,
    10,
    16000,
    100,
    16000,
    100,
    962335,
    18,
    2780678,
    6,
    442008,
    1,
    52538055,
    3756,
    18,
    267929,
    18,
    76433006,
    8868,
    18,
    52948122,
    18,
    1995836,
    36,
    3227919,
    12,
    901022,
    1,
    166917843,
    4307,
    36,
    284546,
    36,
    158221314,
    26549,
    36,
    74698472,
    36,
    333849714,
    1,
    254006273,
    72,
    2174038,
    72,
    2261318,
    64571,
    4,
    207616,
    8310,
    4,
    1293828,
    28716,
    63,
    0,
    1,
    1006041,
    43623,
    251,
    0,
    1
  ],
  "constitution": {
      "anchor": {
          "dataHash": "ca41a91f399259bcefe57f9858e91f6d00e1a38d6d9c63d4052914ea7bd70cb2",
          "url": "ipfs://bafkreifnwj6zpu3ixa4siz2lndqybyc5wnnt3jkwyutci4e2tmbnj3xrdm"
      },
      "script": "fa24fb305126805cf2164c161d852a0e7330cf988f1fe558cf7d4a64"
  },
  "committee": {
    "members": {
        "scriptHash-df0e83bde65416dade5b1f97e7f115cc1ff999550ad968850783fe50": 580,
        "scriptHash-b6012034ba0a7e4afbbf2c7a1432f8824aee5299a48e38e41a952686": 580,
        "scriptHash-ce8b37a72b178a37bbd3236daa7b2c158c9d3604e7aa667e6c6004b7": 580,
        "scriptHash-f0dc2c00d92a45521267be2d5de1c485f6f9d14466d7e16062897cf7": 580,
        "scriptHash-349e55f83e9af24813e6cb368df6a80d38951b2a334dfcdf26815558": 580,
        "scriptHash-84aebcfd3e00d0f87af918fc4b5e00135f407e379893df7e7d392c6a": 580,
        "scriptHash-e8165b3328027ee0d74b1f07298cb092fd99aa7697a1436f5997f625": 580
    },
    "threshold": {
      "numerator": 2,
      "denominator": 3
    }
  }
}'''

config = '''{
  "AlonzoGenesisFile": "alonzo-genesis.json",
  "AlonzoGenesisHash": "7e94a15f55d1e82d10f09203fa1d40f8eede58fd8066542cf6566008068ed874",
  "ByronGenesisFile": "byron-genesis.json",
  "ByronGenesisHash": "5f20df933584822601f9e3f8c024eb5eb252fe8cefb24d1317dc3d432e940ebb",
  "ConwayGenesisFile": "conway-genesis.json",
  "ConwayGenesisHash": "15a199f895e461ec0ffc6dd4e4028af28a492ab4e806d39cb674c88f7643ef62",
  "EnableP2P": true,
  "LastKnownBlockVersion-Alt": 0,
  "LastKnownBlockVersion-Major": 3,
  "LastKnownBlockVersion-Minor": 0,
  "MaxKnownMajorProtocolVersion": 2,
  "MinNodeVersion": "10.1.4",
  "PeerSharing": false,
  "Protocol": "Cardano",
  "RequiresNetworkMagic": "RequiresNoMagic",
  "ShelleyGenesisFile": "shelley-genesis.json",
  "ShelleyGenesisHash": "1a3be38bcbb7911969283716ad7aa550250226b76a61fc51cc9a9a35d9276d81",
  "TargetNumberOfActivePeers": 20,
  "TargetNumberOfEstablishedPeers": 40,
  "TargetNumberOfKnownPeers": 100,
  "TargetNumberOfRootPeers": 100,
  "TraceAcceptPolicy": true,
  "TraceBlockFetchClient": false,
  "TraceBlockFetchDecisions": false,
  "TraceBlockFetchProtocol": false,
  "TraceBlockFetchProtocolSerialised": false,
  "TraceBlockFetchServer": false,
  "TraceChainDb": true,
  "TraceChainSyncBlockServer": false,
  "TraceChainSyncClient": false,
  "TraceChainSyncHeaderServer": false,
  "TraceChainSyncProtocol": false,
  "TraceConnectionManager": true,
  "TraceDNSResolver": true,
  "TraceDNSSubscription": true,
  "TraceDiffusionInitialization": true,
  "TraceErrorPolicy": true,
  "TraceForge": true,
  "TraceHandshake": true,
  "TraceInboundGovernor": true,
  "TraceIpSubscription": true,
  "TraceLedgerPeers": true,
  "TraceLocalChainSyncProtocol": false,
  "TraceLocalConnectionManager": true,
  "TraceLocalErrorPolicy": true,
  "TraceLocalHandshake": true,
  "TraceLocalRootPeers": true,
  "TraceLocalTxSubmissionProtocol": false,
  "TraceLocalTxSubmissionServer": false,
  "TraceMempool": false,
  "TraceMux": false,
  "TracePeerSelection": true,
  "TracePeerSelectionActions": true,
  "TracePublicRootPeers": true,
  "TraceServer": true,
  "TraceTxInbound": false,
  "TraceTxOutbound": false,
  "TraceTxSubmissionProtocol": false,
  "TracingVerbosity": "NormalVerbosity",
  "TurnOnLogMetrics": true,
  "TurnOnLogging": true,
  "UseTraceDispatcher": false,
  "defaultBackends": [
    "KatipBK"
  ],
  "defaultScribes": [
    [
      "StdoutSK",
      "stdout"
    ]
  ],
  "hasEKG": 12788,
  "hasPrometheus": [
    "127.0.0.1",
    12798
  ],
  "minSeverity": "Info",
  "options": {
    "mapBackends": {
      "cardano.node.metrics": [
        "EKGViewBK"
      ],
      "cardano.node.resources": [
        "EKGViewBK"
      ]
    },
    "mapSubtrace": {
      "cardano.node.metrics": {
        "subtrace": "Neutral"
      }
    }
  },
  "rotation": {
    "rpKeepFilesNum": 10,
    "rpLogLimitBytes": 5000000,
    "rpMaxAgeHours": 24
  },
  "setupBackends": [
    "KatipBK"
  ],
  "setupScribes": [
    {
      "scFormat": "ScText",
      "scKind": "StdoutSK",
      "scName": "stdout",
      "scRotation": null
    }
  ] 
}'''
