# World of Coffeebot

Frontend setup (taken from [here](https://github.com/raphamorim/wasm-and-rust)):

1. Setup the build environment (TODO maybe most of this section can just be replaced with `brew install emscripten`)

Rustup is an official Rust project that allows us to install, manage, and update multiple Rust toolchains.

```shell
curl https://sh.rustup.rs -sSf | sh
```

After we’ll be prompted to run the following command to update the current shell with the changes:

```shell
source $HOME/.cargo/env
```

Add the wasm32-unknown-emscripten compile target via rustup as well:

```shell
rustup target add wasm32-unknown-emscripten
```

Set up Emscripten via emsdk. We’ll use the incoming version of Emscripten in order to get the best output.

```shell
# Make sure to have cmake installed before running this:
# - Ubuntu/Debian: apt install cmake
# - MacOS X : brew install cmake
curl https://s3.amazonaws.com/mozilla-games/emscripten/releases/emsdk-portable.tar.gz | tar -zxv -C ~/
cd ~/emsdk-portable
./emsdk update
./emsdk install sdk-incoming-64bit
./emsdk activate sdk-incoming-64bit
```

Emscripten is installed.

The last command will instruct us how to add the binaries to our path for permanent usage, or we can just source `./emsdk_env.sh` for temporary fun.

```shell
$ emcc -v
emcc (Emscripten gcc/clang-like replacement + linker emulating GNU ld) 1.37.22
clang version 4.0.0 (https://github.com/kripken/emscripten-fastcomp-clang.git 3659f873b523e5fc89ffa16baab8901fbd084251) (https://github.com/kripken/emscripten-fastcomp.git de9659961c692174fc4651a6ea0720236e4c4739) (emscripten 1.37.22 : 1.37.22)
Target: x86_64-apple-darwin17.2.0
Thread model: posix
InstalledDir: /Users/raphael.amorim/emsdk-portable/clang/fastcomp/build_incoming_64/bin
INFO:root:(Emscripten: Running sanity checks)
```

2. Get cargo-web and rust nightly

```shell
$ rustup override set nightly
$ cargo install cargo-web
```

3. Build the project

