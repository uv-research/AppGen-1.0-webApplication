tsconfigapp = """{
  "extends": "../tsconfig.json",
  "compilerOptions": {
    "outDir": "../out-tsc/app",
    "types": []
  },
  "exclude": [
    "test.ts",
    "**/*.spec.ts"
  ]
}
"""