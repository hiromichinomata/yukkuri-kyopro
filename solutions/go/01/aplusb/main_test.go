package main

import (
	"bytes"
	"os/exec"
	"testing"
)

func TestAplusb(t *testing.T) {
	cmd := exec.Command("go", "run", ".")
	cmd.Stdin = bytes.NewBufferString("3 5\n")
	var out bytes.Buffer
	cmd.Stdout = &out
	if err := cmd.Run(); err != nil {
		t.Fatal(err)
	}
	if got := out.String(); got != "8\n" {
		t.Fatalf("got %q, want %q", got, "8\n")
	}
}
